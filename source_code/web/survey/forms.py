from .models import Survey, Question, Option
from django.forms import ModelForm
from django.forms.models import modelformset_factory, inlineformset_factory


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


OptionCreationFormSet = inlineformset_factory(Question, Option, OptionCreationForm)
