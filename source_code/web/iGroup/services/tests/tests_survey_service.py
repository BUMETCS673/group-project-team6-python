from django.test import TestCase
from survey.models import Survey, Question, Option
from iGroup.models import Instance
from account.models import Instructor
from services.services import SurveyService
from ..app.survey import Survey as SurveyClass
from ..app.question import SingleChoiceQuestion, MultipleChoiceQuestion


class TestSurveyService(TestCase):

	def setUp(self):
		self.instructor_1 = Instructor.objects.create(username='testuser123', password='dd23@qwd')
		self.instance = Instance.objects.create(instance_name="test 1", instructor=self.instructor_1, slug="test-1")
		self.survey = Survey.objects.create(survey_name='test survey', instance=self.instance)
		for i in range(10):
			question = Question.objects.create(question_type="MULTIPLE", question_name='', description='', weight=3,
			                                   max_choice=3, question_index=i, survey=self.survey)
			option_1 = Option.objects.create(choice_index=0, choice_name=f"{i}-1", question=question)
			option_2 = Option.objects.create(choice_index=1, choice_name=f"{i}-2", question=question)
			option_3 = Option.objects.create(choice_index=2, choice_name=f"{i}-3", question=question)

	def test_create_survey_service(self):
		survey_service = SurveyService(survey_obj=self.survey,
		                               question_obj_set=Question.objects.filter(survey=self.survey))
		self.assertIsInstance(survey_service, SurveyService)

		# check if the survey it creates is valid
		survey_service.build_survey()

		# check number of questions
		self.assertEqual(len(survey_service.survey.questions), 10)



