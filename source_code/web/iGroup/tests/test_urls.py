from django.test import TestCase
from django.urls import reverse, resolve
from iGroup.views import index, create_instance, detail_instance, config_instance


class TestUrls(TestCase):
	def setUp(self):
		self.instance_home_url = reverse('iGroup:home')
		self.instance_detail_url = reverse('iGroup:detail', args=['test-1'])
		self.instance_create_url = reverse('iGroup:create')
		self.instance_config_url = reverse('iGroup:config', args=['test-1'])

	def test_instance_home_url_is_resolved(self):
		self.assertEqual(resolve(self.instance_home_url).func, index)

	def test_instance_detail_url_is_resolved(self):
		self.assertEqual(resolve(self.instance_detail_url).func, detail_instance)

	def test_instance_create_url_is_resolved(self):
		self.assertEqual(resolve(self.instance_create_url).func, create_instance)

	def test_instance_config_url_is_resolved(self):
		self.assertEqual(resolve(self.instance_config_url).func, config_instance)
