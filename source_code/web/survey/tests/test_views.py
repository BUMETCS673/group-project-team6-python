from django.test import TestCase, Client
from django.urls import reverse, resolve
from iGroup.models import Instance, ConfigInstance
from account.models import Instructor
from survey.models import Survey


class TestViewSurvey(TestCase):
	"""test cases for related survey functions"""

	def setUp(self):
		"""set up for survey test"""
		self.instructor = Instructor.objects.create(username='testuser123', password='dd23@qwd')
		self.intruder = Instructor.objects.create(username='testuser234', password='dd23@dsaqwd')

		self.instructor_login = Client()
		self.instructor_login.force_login(self.instructor)  # force to logged in

		self.intruder_login = Client()
		self.intruder_login.force_login(self.intruder)  # force login other user

		self.not_login = Client()  # not logged in user

		# create instance
		self.instance = Instance.objects.create(instance_name="test 1", instructor=self.instructor, slug="test-1")

		# urls: set up for survey
		self.create_survey = reverse('survey:create_survey', args=['test-1'])

	def test_create_a_survey(self):
		"""test for creating a survey"""

		data = {
			'survey_name': 'test-survey'

		}
		response = self.instructor_login.post(
			path=self.create_survey,
			data=data
		)
		# check in the database
		self.assertEqual(response.status_code, 302)
		self.assertEqual(len(Survey.objects.filter(instance=self.instance)), 1)

	def test_create_a_survey_intruder(self):
		"""test for creating a survey"""

		data = {
			'survey_name': 'test-survey'

		}
		response = self.intruder_login.post(
			path=self.create_survey,
			data=data
		)
		# check in the database
		self.assertEqual(response.status_code, 404)
		self.assertEqual(len(Survey.objects.filter(instance=self.instance)), 0)

	def test_create_a_survey_not_login(self):
		"""test for creating a survey"""

		data = {
			'survey_name': 'test-survey'

		}
		response = self.not_login.post(
			path=self.create_survey,
			data=data
		)
		# check in the database
		self.assertEqual(response.status_code, 302) # redirect to login page
		self.assertEqual(len(Survey.objects.filter(instance=self.instance)), 0)

	def test_view_survey_index(self):
		"""view the survey index"""
		# first create a survey
		survey = Survey.objects.create(survey_name='survey-1', instance=self.instance)
		survey_id = survey.survey_id
		response = self.instructor_login.get(
			path=reverse('survey:survey_index', args=[survey_id])
		)
		self.assertEqual(response.status_code, 200)

	def test_intruder_view_survey_index(self):
		"""the intruder try to view the survey"""
		survey = Survey.objects.create(survey_name='survey-1', instance=self.instance)
		survey_id = survey.survey_id
		response = self.intruder_login.get(
			path=reverse('survey:survey_index', args=[survey_id])
		)
		self.assertEqual(response.status_code, 404)

	def test_not_login_view_survey_index(self):
		"""the not login user try to view the survey"""
		survey = Survey.objects.create(survey_name='survey-1', instance=self.instance)
		survey_id = survey.survey_id
		response = self.not_login.get(
			path=reverse('survey:survey_index', args=[survey_id])
		)
		self.assertEqual(response.status_code, 302)


class TestViewQuestion(TestCase):
	"""test cases for related question functions"""