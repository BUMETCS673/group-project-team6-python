from django.test import TestCase, Client
from django.urls import reverse, resolve
from iGroup.models import Instance, ConfigInstance
from account.models import Instructor
from survey.models import Survey


class TestViews(TestCase):

	def setUp(self):
		self.instructor_1 = Instructor.objects.create(username='testuser123', password='dd23@qwd')
		self.instructor_2 = Instructor.objects.create(username='testuser234', password='dd23@dsaqwd')
		self.client_login = Client()
		self.client_login.force_login(self.instructor_1)  # force to logged in

		self.client_alien_login = Client()
		self.client_alien_login.force_login(self.instructor_2)  # force login alien

		self.client_not_login = Client()

		# create instance
		self.instance = Instance.objects.create(instance_name="test 1", instructor=self.instructor_1, slug="test-1")
		# create survey link to this instance
		self.survey = Survey.objects.create(survey_name='test survey', instance=self.instance)

		self.instance_home_url = reverse('iGroup:home')
		self.instance_detail_url = reverse('iGroup:detail', args=['test-1'])
		self.instance_detail_url_not_match = reverse('iGroup:detail', args=['test-2'])
		self.instance_create_url = reverse('iGroup:create')
		self.instance_config_url = reverse('iGroup:config', args=['test-1'])

	def test_login_client_instance_home_GET(self):
		"""login client test"""
		response = self.client_login.get(path=self.instance_home_url)
		# check status code
		self.assertEqual(response.status_code, 200)
		# check template
		self.assertTemplateUsed(response, 'iGroup/home.html')

	def test_not_login_client_instance_home_GET(self):
		"""not login client test"""
		response = self.client_not_login.get(path=self.instance_home_url)
		# check status code
		self.assertEqual(response.status_code, 302)

	def test_login_client_instance_detail_GET_not_found(self):
		response = self.client_login.get(path=self.instance_detail_url_not_match)

		# check status code
		self.assertEqual(response.status_code, 404)

	def test_not_login_client_instance_detail_GET_not_found(self):
		response = self.client_not_login.get(path=self.instance_detail_url)

		# check status code
		self.assertEqual(response.status_code, 302)

	def test_unauthorized_login_client_instance_detail_GET(self):
		response = self.client_alien_login.get(path=self.instance_detail_url)

		# check status
		self.assertNotEqual(response.status_code, 200)
		self.assertTemplateNotUsed(response, 'iGroup/instance.html')

	def test_login_client_instance_detail_GET_valid(self):
		response = self.client_login.get(path=self.instance_detail_url)

		# check status
		self.assertEqual(response.status_code, 200)
		# check templates
		self.assertTemplateUsed(response, 'iGroup/instance.html')

	def test_not_login_client_instance_detail_GET_valid(self):
		response = self.client_not_login.get(path=self.instance_detail_url)

		# check status
		self.assertEqual(response.status_code, 302)
		# check templates
		self.assertTemplateNotUsed(response, 'iGroup/instance.html')

	def test_login_client_instance_create_GET(self):
		response = self.client_login.get(path=self.instance_create_url)
		# check status
		self.assertEqual(response.status_code, 200)
		# check template
		self.assertTemplateUsed(response, 'iGroup/instance_create.html')

	def test_not_login_client_instance_create_GET(self):
		response = self.client_not_login.get(path=self.instance_create_url)
		# check status
		self.assertEqual(response.status_code, 302)
		# check template
		self.assertTemplateNotUsed(response, 'iGroup/instance_create.html')

	def test_login_client_instance_create_POST_add_new_instance(self):
		response = self.client_login.post(path=self.instance_create_url,
		                                  data={'instance_name': "test add new instance"})
		# code
		self.assertEqual(response.status_code, 302)

		# check it is in the database
		self.assertTrue(Instance.objects.filter(instance_name='test add new instance'))

	def test_not_login_client_instance_create_POST_add_new_instance(self):
		response = self.client_not_login.post(path=self.instance_create_url,
		                                      data={'instance_name': "test add new instance again"})
		# code
		self.assertEqual(response.status_code, 302)
		# should no store in the database
		self.assertFalse(Instance.objects.filter(instance_name='test add new instance again'))

	"""
	prerequisite: survey creation
	"""

	def test_login_client_instance_config_GET_has_survey(self):
		response = self.client_login.get(path=self.instance_config_url)
		# code
		self.assertEqual(response.status_code, 200)
		# template
		self.assertTemplateUsed(response, 'iGroup/config.html')

	def test_not_login_client_instance_config_GET_has_survey(self):
		response = self.client_not_login.get(path=self.instance_config_url)
		# code, redirect
		self.assertEqual(response.status_code, 302)

	def test_alien_login_client_instance_config_GET_has_survey(self):
		response = self.client_alien_login.get(path=self.instance_config_url)
		# status code
		self.assertEqual(response.status_code, 404)

	def test_login_client_instance_config_POST_create_config_has_survey(self):
		response = self.client_login.post(path=self.instance_config_url, data={'max_num_pass': 10, 'num_group': 10})
		# code for redirect
		self.assertEqual(response.status_code, 302)
		# check database
		self.assertTrue(
			(ConfigInstance.objects.first().max_num_pass == 10) and (ConfigInstance.objects.first().num_group == 10))

	def test_not_login_client_instance_config_POST_create_config(self):
		response = self.client_not_login.get(path=self.instance_config_url)
		# code, redirect
		self.assertEqual(response.status_code, 302)

	def test_alien_login_client_instance_config_POST_create_config(self):
		response = self.client_alien_login.get(path=self.instance_config_url)

		# status code, forbid this user to post
		self.assertEqual(response.status_code, 404)
