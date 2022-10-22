import unittest
from code.app import question


# test single choice function
class test_single_choice_question(unittest.TestCase):
    # set up test objects
    def setUp(self):
        self.question1 = question.SingleChoiceQuestion(question_name="q1", description="test q1", weight=1,
                                                       choices=None)
        self.question2 = question.SingleChoiceQuestion(question_name="q2", description="test q2", weight=2,
                                                       choices=None)
        self.question3 = question.SingleChoiceQuestion(question_name="q3", description="test q3", weight=3,
                                                       choices=None)

    # test single choice question init
    def test_single_choice_question_init(self):
        # test question_name
        self.assertEqual(self.question1.question_name, "q1")
        self.assertEqual(self.question2.question_name, "q2")
        self.assertEqual(self.question3.question_name, "q3")

        # test description
        self.assertEqual(self.question1.description, "test q1")
        self.assertEqual(self.question2.description, "test q2")
        self.assertEqual(self.question3.description, "test q3")

        # test weight
        self.assertEqual(self.question1.weight, 1)
        self.assertEqual(self.question2.weight, 2)
        self.assertEqual(self.question3.weight, 3)

        # test choice
        self.assertEqual(self.question1.choices, [])
        self.assertEqual(self.question2.choices, [])
        self.assertEqual(self.question3.choices, [])

        # test type
        self.assertTrue(isinstance(self.question1, question.Question))
        self.assertTrue(isinstance(self.question2, question.Question))
        self.assertTrue(isinstance(self.question3, question.Question))

    # Test get_weight
    def test_get_weight(self):
        self.assertEqual(self.question1.get_weight(), 1)
        self.assertEqual(self.question2.get_weight(), 2)

    # test add_choice
    def test_add_choice(self):
        self.question1.add_choice("A")
        self.question1.add_choice("B")
        self.question1.add_choice("C")
        self.assertEqual(self.question1.choices, ["A", "B", "C"])

        self.question2.add_choice("1")
        self.question2.add_choice("2")
        self.question2.add_choice("3")
        self.assertEqual(self.question2.choices, ["1", "2", "3"])

    # test get_question_type
    def test_get_question_type(self):
        self.assertEqual(self.question1.get_question_type(), "single")
        self.assertEqual(self.question2.get_question_type(), "single")
        self.assertEqual(self.question3.get_question_type(), "single")

    # test_delete_choice, original code not finished
    """
    def test_delete_choice(self):

        self.question1.delete_choice(1)
        self.assertEqual(self.question1.choices, ["A", "C"])

        self.question2.delete_choice(0)
        self.assertEqual(self.question2.choices, ["2", "3"])
    """

    # Test get_all_choice
    def test_get_all_choice(self):
        self.question3.add_choice("A")
        self.question3.add_choice("B")
        self.question3.add_choice("C")
        self.assertEqual(self.question3.get_all_choice(), ["A", "B", "C"])

    # Test get_choice_size
    def test_get_choice_size(self):
        self.assertEqual(self.question3.get_choice_size(), 3)


# Test multiple choice question class
class test_multiple_choice_question(unittest.TestCase):
    # set up test objects
    def setUp(self):
        self.question1 = question.SingleChoiceQuestion(question_name="q1", description="test q1", weight=1,
                                                       choices=None, )
        self.question2 = question.SingleChoiceQuestion(question_name="q2", description="test q2", weight=2,
                                                       choices=None)
        self.question3 = question.SingleChoiceQuestion(question_name="q3", description="test q3", weight=3,
                                                       choices=None)


if __name__ == '__main__':
    unittest.main()
