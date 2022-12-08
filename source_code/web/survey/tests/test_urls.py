from django.test import TestCase
from django.urls import reverse, resolve
from survey import views_survey, views_question, views_upload, views_option, views_answer, views_student


class TestUrls(TestCase):
	"""test cases need to start with 'test' """

	def setUp(self):
		# set up for survey
		self.create_survey = reverse('survey:create_survey', args=['test-instance-1'])
		self.survey_index = reverse('survey:survey_index', args=['1'])
		self.lock_survey = reverse('survey:lock_survey', args=['1'])
		self.get_survey_link = reverse('survey:get_survey_link', args=['1'])

		# set up for question
		self.question_list = reverse('survey:question_list', args=['1'])
		self.add_question = reverse('survey:add_question', args=['1'])
		self.upload_questions_csv = reverse('survey:upload_questions_csv', args=['1'])
		self.edit_question = reverse('survey:edit_question', args=['1', '1'])

	# options

	"""test survey urls"""

	def test_create_survey_url_is_resolved(self):
		self.assertEqual(resolve(self.create_survey).func, views_survey.create_survey)

	def test_survey_index_url_is_resolved(self):
		self.assertEqual(resolve(self.survey_index).func, views_survey.survey_index)

	def test_lock_survey_url_is_resolved(self):
		self.assertEqual(resolve(self.lock_survey).func, views_survey.lock_survey)

	def test_get_survey_link_url_is_resolved(self):
		self.assertEqual(resolve(self.get_survey_link).func, views_survey.get_survey_link)

	"""test survey urls end"""

	"""test question urls"""

	def test_question_list_url_is_resolved(self):
		self.assertEqual(resolve(self.question_list).func, views_question.question_list)

	def test_add_question_url_is_resolved(self):
		self.assertEqual(resolve(self.add_question).func, views_question.add_question)

	def test_upload_questions_csv_url_is_resolved(self):
		self.assertEqual(resolve(self.upload_questions_csv).func, views_upload.upload_questions_csv)

	def test_edit_question_url_is_resolved(self):
		self.assertEqual(resolve(self.edit_question).func, views_question.edit_question)

	"""test question urls end"""
