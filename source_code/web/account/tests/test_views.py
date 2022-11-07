from django.test import TestCase, Client
from django.urls import reverse, resolve
from account.models import Instructor
from account.views import register


class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.register_url = reverse('register')
		self.login_url = reverse('login')
		self.logout_url = reverse('logout')
		self.instructor_form = {
			'username': "test123",
			'password': 'fi3un@',
			'first_name': 'first',
			'last_name': 'last'
		}

	def test_register_instructor_GET(self):
		response = self.client.get(self.register_url)
		# status code check
		self.assertEquals(response.status_code, 200)
		# template check
		self.assertTemplateUsed(response, 'registration/register.html')

	def test_login_instructor_GET(self):
		response = self.client.get(self.login_url)
		# status code check
		self.assertEquals(response.status_code, 200)
		# template check
		self.assertTemplateUsed(response, 'registration/login.html')

	def test_logout_instructor_GET(self):
		response = self.client.get(self.login_url)
		# status code check
		self.assertEquals(response.status_code, 200)

	def test_register_instructor_POST_add_new_user(self):
		response = self.client.post(self.register_url, self.instructor_form)
		# check status code
		self.assertEquals(response.status_code, 200)

	def test_register_instructor_POST_no_data(self):
		response = self.client.post(self.register_url)
		self.assertEqual(response.status_code, 200)
		#make sure not adding to the database
		self.assertEqual(Instructor.objects.count(),0)

