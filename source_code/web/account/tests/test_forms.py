from django.test import TestCase
from account.forms import InstructorCreationForm


class TestForms(TestCase):

	def setUp(self):
		self.valid_email = "test@bu.com"
		self.invalid_email = "dsadfsf"
		self.valid_password = "gri4u@wqA"
		self.invalid_password = "123"
		self.first_name = "first"
		self.last_name = "last"

	def test_instructor_creation_form_valid_data(self):
		form = InstructorCreationForm(
			data={
				'username': 'test',
				'email': self.valid_email,
				'password1': self.valid_password,
				'password2': self.valid_password,
				'first_name': self.first_name,
				'last_name': self.last_name
			}
		)
		self.assertTrue(form.is_valid())

	def test_instructor_creation_form_conflict_password(self):

		form = InstructorCreationForm(
			data={
				'username': 'test',
				'email': self.valid_email,
				'password1': self.valid_password,
				'password2': "different",
				'first_name': self.first_name,
				'last_name': self.last_name
			}
		)
		self.assertFalse(form.is_valid())

	def test_instructor_creation_form_no_data(self):

		form = InstructorCreationForm(
			data={
			}
		)
		self.assertFalse(form.is_valid())

	def test_instructor_creation_form_easy_password(self):

		form = InstructorCreationForm(
			data={
				'username': 'test',
				'email': self.valid_email,
				'password1': '123',
				'password2': "123",
				'first_name': self.first_name,
				'last_name': self.last_name
			}
		)
		self.assertFalse(form.is_valid())

	def test_instructor_creation_form_invalid_email(self):

		form = InstructorCreationForm(
			data={
				'username': 'test',
				'email': self.invalid_email,
				'password1': '123',
				'password2': "123",
				'first_name': self.first_name,
				'last_name': self.last_name
			}
		)
		self.assertFalse(form.is_valid())