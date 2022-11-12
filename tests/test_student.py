import unittest
from source_code.app import user


class student_test_sheet(unittest.TestCase):
    def setUp(self):
        self.student1 = user.Student(user_id="001", name="Jessie", email="jessie@doe.com")
        self.student2 = user.Student(user_id="002", name="James", email="james@doe.com")
        self.student3 = user.Student(user_id="003", name="jack", email="jack@doe.com")
        self.student4 = user.Student(user_id="004", name="JANE", email="jane@doe.com")
        self.student5 = user.Student(user_id="005", name="JOHN", email="john@doe.com")
        self.student6 = user.Student(user_id="006", name="JaGeR", email="jager@doe.com")
        self.student7 = user.Student(user_id="007", name="jessica", email="jessica@doe.com")

    def test01_ID(self):
        self.assertEqual(self.student1.get_ID(), "001")
        self.assertEqual(self.student2.get_ID(), "002")
        self.assertEqual(self.student3.get_ID(), "003")
        self.assertEqual(self.student4.get_ID(), "004")
        self.assertEqual(self.student5.get_ID(), "005")
        self.assertEqual(self.student6.get_ID(), "006")
        self.assertEqual(self.student7.get_ID(), "007")

    def test02_name_PT_1(self):
        self.assertEqual(self.student1.get_name().lower(), "Jessie".lower())
        self.assertEqual(self.student2.get_name().lower(), "JAMES".lower())
        self.assertEqual(self.student3.get_name().lower(), "jack".lower())
        self.assertEqual(self.student4.get_name().lower(), "jane".lower())
        self.assertEqual(self.student5.get_name().lower(), "JOHN".lower())
        self.assertEqual(self.student6.get_name().lower(), "jager".lower())
        self.assertEqual(self.student7.get_name().lower(), "JESSICA".lower())

    def test03_name_PT_2(self):
        self.assertTrue(self.student1.get_name() == "Jessie")
        self.assertFalse(self.student2.get_name() == "JAMES")
        self.assertTrue(self.student3.get_name() == "jack")
        self.assertFalse(self.student4.get_name() == "jane")
        self.assertTrue(self.student5.get_name() == "JOHN")
        self.assertFalse(self.student6.get_name() == "jager")
        self.assertFalse(self.student7.get_name() == "JESSICA")

    def test04_email(self):
        self.assertEqual(self.student1.get_email(), "jessie@doe.com")
        self.assertEqual(self.student2.get_email(), "james@doe.com")
        self.assertEqual(self.student3.get_email(), "jack@doe.com")
        self.assertEqual(self.student4.get_email(), "jane@doe.com")
        self.assertEqual(self.student5.get_email(), "john@doe.com")
        self.assertEqual(self.student6.get_email(), "jager@doe.com")
        self.assertEqual(self.student7.get_email(), "jessica@doe.com")


if __name__ == '__main__':
    unittest.main()
