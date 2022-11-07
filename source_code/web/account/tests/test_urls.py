from django.test import TestCase
from django.urls import reverse, resolve
from account.views import register, home
from django.contrib.auth.views import LoginView, LogoutView


class TestUrls(TestCase):

	def test_register_url_is_resolved(self):
		url = reverse('register')
		self.assertEqual(resolve(url).func, register)

	def test_login_url_is_resolved(self):
		url = reverse('login')
		print(resolve(url).func)
		self.assertEqual(resolve(url).func.view_class, LoginView)

	def test_logout_url_is_resolved(self):
		url = reverse('logout')
		self.assertEqual(resolve(url).func.view_class, LogoutView)


