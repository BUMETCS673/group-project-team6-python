from .models import Survey, Question, Option, AnswerSheet, ChoiceMultiple, ChoiceSingle
from account.models import Student
from django.forms import Form
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from django.forms.models import modelformset_factory, inlineformset_factory
from django.forms.models import BaseInlineFormSet, BaseModelFormSet, BaseFormSet, ValidationError, BaseModelForm
from django import forms


class SurveyCreationForm(ModelForm):
	"""Survey form to create a survey"""

	class Meta:
		model = Survey
		fields = ('survey_name',)


class QuestionCreationForm(ModelForm):
	"""question form to create a question in survey"""

	class Meta:
		model = Question
		fields = ('question_type', 'question_name', 'description', 'weight', 'max_choice',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		if not self.instance.survey.modify:
			for field in self.fields:
				self.fields[field].disabled = True


QuestionCreationFormSet = modelformset_factory(Question, form=QuestionCreationForm, extra=0)


class OptionCreationForm(ModelForm):
	"""question option form"""

	class Meta:
		model = Option
		fields = ('choice_name',)

	def __init__(self, *args, question, **kwargs):
		super(OptionCreationForm, self).__init__(*args, **kwargs)
		self.question = question

	def clean(self):
		"""form validation"""
		data = self.cleaned_data
		option_name = data.get('choice_name')

		# find the duplication instances within current user's all instance
		options = Option.objects.filter(choice_name=option_name, question=self.question)
		print(self.question)
		qs = options.filter(choice_name=option_name)
		if qs.exists():
			self.add_error("choice_name", f'{option_name} is already in this question')
		return data


class BaseOptionFormSet(BaseModelFormSet):

	def __init__(self, *args, **kwargs):
		super(BaseOptionFormSet, self).__init__(*args, **kwargs)

	def clean(self):
		"""check duplicate choice name"""
		super(BaseOptionFormSet, self).clean()
		option_names = set()
		for form in self.forms:
			option_name = form.cleaned_data['choice_name']
			if option_name in option_names:
				form.add_error('choice_name', "error")  # need to find a way to report such error
			option_names.add(option_name)


OptionCreationFormSet = \
	modelformset_factory(Option, fields=('choice_name',), formset=BaseOptionFormSet, extra=0)


class StudentCreationFrom(ModelForm):
	"""store student info"""

	class Meta:
		model = Student
		fields = ('email', 'name')

	def clean_email(self):
		"""email validation"""
		email = self.cleaned_data['email']
		return email

	def clean_name(self):
		"""student name validation"""
		name = self.cleaned_data['name']
		return name

	def clean(self):
		"""general clean"""
		pass


class SurveyForm(forms.Form):
	"""survey answer form, should show all the available choices"""

	def __init__(self, *args, **kwargs):

		self.student = kwargs.pop('student', None)  # set student
		self.survey = kwargs.pop('survey', None)
		super().__init__(*args, **kwargs)
		self.questions = self.survey.get_questions_set()
		for question in self.questions:
			# all the option of the question
			choices = [(option.choice_index, option.choice_name) for index, option in
			           enumerate(question.get_options_set_order_by_index())]
			if question.question_type == "SINGLE":

				self.fields[f'question_single_{question.question_index}'] = forms.ChoiceField(widget=forms.RadioSelect,
				                                                                              choices=choices)
				self.fields[f'question_single_{question.question_index}'].label = question.question_name
			elif question.question_type == "MULTIPLE":
				choices = [(-1, 'no preference')] + choices
				# multiple choice, list max number of allowed choice
				for option_index in range(question.max_choice):  # enumerate(question.get_options_set_order_by_index()):
					self.fields[
						f'question_multiple_{question.question_index}_choice_{option_index}'] = \
						forms.ChoiceField(choices=choices)
					self.fields[
						f'question_multiple_{question.question_index}_choice_{option_index}'].label = \
						f'question_{question.question_index}_choice_{option_index}'

	def save(self):
		data = self.cleaned_data
		# should be get or created
		# answer_sheet = AnswerSheet(survey=self.survey, student=self.student)
		answer_sheet = AnswerSheet.objects.get_or_create(survey=self.survey, student=self.student)[0]

		# answer_sheet.save()

		for question in self.survey.get_questions_set():
			if question.question_type == "SINGLE":
				choice_index = data[f'question_single_{question.question_index}'][0]
				option = Option.objects.get(choice_index=choice_index,
				                            question=question)
				choice = ChoiceSingle(option=option,
				                      question=question,
				                      answer_sheet=answer_sheet)
				#choice.save()
			# answer_sheet.answer_single_choice.add(choice)
			elif question.question_type == "MULTIPLE":
				rank = 0  # init
				for option_index, _ in enumerate(question.get_options_set_order_by_index()):
					choice_index = data[f'question_multiple_{question.question_index}_choice_{option_index}']
					if choice_index == '-1':
						continue
					option = Option.objects.get(question=question,
					                            choice_index=choice_index)

					choice = ChoiceMultiple(option=option,
					                        rank=rank,
					                        answer_sheet=answer_sheet)
					choice.save()
					# answer_sheet.answer_multiple_choice.add(choice)
					rank += 1
		# answer_sheet.save()

		return answer_sheet


class SurveyAnswerForm(forms.Form):

	def __init__(self, *args, **kwargs):
		self.student = kwargs.pop('student', None)  # set student
		self.survey = kwargs.pop('survey', None)
		super().__init__(*args, **kwargs)
		self.questions = self.survey.get_questions_set()




class LockSurveyForm(Form):
	lock_modify = forms.BooleanField(label="sure to lock the survey? you can not modify it later")
