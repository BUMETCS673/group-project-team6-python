from .models import Survey, Question, Option
from django.forms import ModelForm
from django.forms.models import modelformset_factory, inlineformset_factory
from django.forms.models import BaseInlineFormSet, BaseModelFormSet, BaseFormSet, ValidationError


class SurveyCreationForm(ModelForm):
	"""Survey form to create a survey"""

	class Meta:
		model = Survey
		fields = ('survey_name',)


class QuestionCreationForm(ModelForm):
	"""question form to create a question in survey"""

	class Meta:
		model = Question
		fields = ('question_type', 'question_name', 'description', 'weight',)


QuestionCreationFormSet = modelformset_factory(Question, form=QuestionCreationForm, extra=0)


class OptionCreationForm(ModelForm):
	"""question option form"""

	class Meta:
		model = Option
		fields = ('choice_name',)

	def __init__(self, question, *args, **kwargs):
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
				form.add_error('choice_name',"error") #need to find a way to report such error
			option_names.add(option_name)



OptionCreationFormSet = \
	modelformset_factory(Option, fields=('choice_name',), formset=BaseOptionFormSet, extra=0)
