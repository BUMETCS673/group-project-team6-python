import unittest
from code.app import question


# test single choice function
class test_single_choice_question(unittest.TestCase):
    # set up test objects
    def setUp(self):
        self.question1 = question.SingleChoiceQuestion(question_name="q1", description="test q1", weight=1,
                                                       choices=["A", "B", "C"])
        self.question2 = question.SingleChoiceQuestion(question_name="q2", description="test q2", weight=2,
                                                       choices=["1", "2", "3"])
        self.question3 = question.SingleChoiceQuestion(question_name="q3", description="test q3", weight=3,
                                                       choices=["A", "B", "C"])

        # special
        self.question4 = question.SingleChoiceQuestion(question_name="", description="", weight=0,
                                                       choices=None)
        self.question5 = question.SingleChoiceQuestion(question_name=None, description=None, weight=None,
                                                       choices=None)

    # test single choice question init
    def test01_single_choice_question_init(self):
        # test question_name
        self.assertEqual("q1", self.question1.question_name)
        self.assertEqual("q2", self.question2.question_name)
        self.assertEqual("q3", self.question3.question_name)

        self.assertEqual("", self.question4.question_name)
        self.assertEqual(None, self.question5.question_name)

        # test description
        self.assertEqual("test q1", self.question1.description)
        self.assertEqual("test q2", self.question2.description)
        self.assertEqual("test q3", self.question3.description)

        self.assertEqual("", self.question4.description)
        self.assertEqual(None, self.question5.description)

        # test weight
        self.assertEqual(1, self.question1.weight)
        self.assertEqual(2, self.question2.weight)
        self.assertEqual(3, self.question3.weight)

        self.assertEqual(0, self.question4.weight)
        self.assertEqual(None, self.question5.weight)

        # test choice
        self.assertEqual(["A", "B", "C"], self.question1.choices)
        self.assertEqual(["1", "2", "3"], self.question2.choices)
        self.assertEqual(["A", "B", "C"], self.question3.choices)

        self.assertEqual([], self.question4.choices)
        self.assertEqual([], self.question5.choices)

        # test type
        self.assertIsInstance(self.question1, question.SingleChoiceQuestion)
        self.assertIsInstance(self.question2, question.SingleChoiceQuestion)
        self.assertIsInstance(self.question3, question.SingleChoiceQuestion)

        self.assertIsInstance(self.question4, question.SingleChoiceQuestion)
        self.assertIsInstance(self.question5, question.SingleChoiceQuestion)

    # Test get_weight
    def test02_get_weight(self):
        self.assertEqual(1, self.question1.get_weight())
        self.assertEqual(2, self.question2.get_weight())
        self.assertEqual(3, self.question3.get_weight())

        self.assertEqual(0, self.question4.get_weight())
        self.assertEqual(None, self.question5.get_weight())

    # test add_choice
    def test03_add_choice(self):
        # add choice
        self.question1.add_choice("D")
        self.question2.add_choice("4")

        # special condition
        self.question1.add_choice(None)
        self.question2.add_choice("")

        # test choice num
        self.assertEqual(4, len(self.question1.choices))
        self.assertEqual(4, len(self.question2.choices))

        # test choices
        self.assertEqual(["A", "B", "C", "D"], self.question1.choices)
        self.assertEqual(["1", "2", "3", "4"], self.question2.choices)

    # test get_question_type
    def test04_get_question_type(self):
        self.assertEqual("single", self.question1.get_question_type())
        self.assertEqual("single", self.question2.get_question_type())
        self.assertEqual("single", self.question3.get_question_type())
        # special
        self.assertEqual("single", self.question4.get_question_type())
        self.assertEqual("single", self.question5.get_question_type())

    # test_delete_choice
    def test05_delete_choice(self):
        # delete choice
        self.question1.delete_choice(1)
        self.question2.delete_choice(0)

        # special condition
        self.question1.delete_choice(9999999)
        self.question2.delete_choice(-1)

        # test choice num
        self.assertEqual(2, len(self.question1.choices))
        self.assertEqual(2, len(self.question2.choices))

        # test choices
        self.assertEqual(["A", "C"], self.question1.choices)
        self.assertEqual(["2", "3"], self.question2.choices)

    # Test get_all_choice
    def test06_get_all_choice(self):
        self.assertEqual(["A", "B", "C"], self.question1.get_all_choice())
        self.assertEqual(["1", "2", "3"], self.question2.get_all_choice())
        self.assertEqual(["A", "B", "C"], self.question3.get_all_choice())
        # special
        self.assertEqual([], self.question4.get_all_choice())
        self.assertEqual([], self.question5.get_all_choice())

    # Test get_choice_size
    def test07_get_choice_size(self):
        self.question1.delete_choice(0)
        self.question1.delete_choice(0)
        self.question2.delete_choice(0)
        self.assertEqual(1, self.question1.get_choice_size())
        self.assertEqual(2, self.question2.get_choice_size())
        self.assertEqual(3, self.question3.get_choice_size())
        # special
        self.assertEqual(0, self.question4.get_choice_size())
        self.assertEqual(0, self.question5.get_choice_size())


# Test multiple choice question class
class test_multiple_choice_question(unittest.TestCase):
    # set up test objects
    def setUp(self):
        self.question1 = question.MultipleChoiceQuestion(question_name="q1", description="test q1", weight=1,
                                                         choices=["A", "B", "C", "D", "E"], max_num_choice=2)
        self.question2 = question.MultipleChoiceQuestion(question_name="q2", description="test q2", weight=2,
                                                         choices=["1", "2", "3", "4", "5"], max_num_choice=3)
        self.question3 = question.MultipleChoiceQuestion(question_name="q3", description="test q3", weight=3,
                                                         choices=["Python", "Java", "C", "C++"], max_num_choice=4)
        self.question4 = question.MultipleChoiceQuestion(question_name="", description="", weight=0,
                                                         choices=None, max_num_choice=-1)
        self.question5 = question.MultipleChoiceQuestion(question_name=None, description=None, weight=None,
                                                         choices=None, max_num_choice=None)

    # test multiple choice question init
    def test09_multiple_choice_question_init(self):
        # test question_name
        self.assertEqual("q1", self.question1.question_name)
        self.assertEqual("q2", self.question2.question_name)
        self.assertEqual("q3", self.question3.question_name)
        self.assertEqual("", self.question4.question_name)
        self.assertEqual(None, self.question5.question_name)

        # test description
        self.assertEqual("test q1", self.question1.description)
        self.assertEqual("test q2", self.question2.description)
        self.assertEqual("test q3", self.question3.description)
        self.assertEqual("", self.question4.description)
        self.assertEqual(None, self.question5.description)

        # test weight
        self.assertEqual(1, self.question1.weight)
        self.assertEqual(2, self.question2.weight)
        self.assertEqual(3, self.question3.weight)
        self.assertEqual(0, self.question4.weight)
        self.assertEqual(None, self.question5.weight)

        # test choice
        self.assertEqual(["A", "B", "C", "D", "E"], self.question1.choices)
        self.assertEqual(["1", "2", "3", "4", "5"], self.question2.choices)
        self.assertEqual(["Python", "Java", "C", "C++"], self.question3.choices)
        self.assertEqual([], self.question4.choices)
        self.assertEqual([], self.question5.choices)

        # test max num choice
        # test choice
        self.assertEqual(2, self.question1.max_num_choice)
        self.assertEqual(3, self.question2.max_num_choice)
        self.assertEqual(4, self.question3.max_num_choice)
        self.assertEqual(2, self.question4.max_num_choice)
        self.assertEqual(2, self.question5.max_num_choice)

        # test type
        self.assertIsInstance(self.question1, question.MultipleChoiceQuestion)
        self.assertIsInstance(self.question2, question.MultipleChoiceQuestion)
        self.assertIsInstance(self.question3, question.MultipleChoiceQuestion)
        self.assertIsInstance(self.question4, question.MultipleChoiceQuestion)
        self.assertIsInstance(self.question5, question.MultipleChoiceQuestion)

    # Test get_weight
    def test10_get_weight(self):
        self.assertEqual(1, self.question1.get_weight())
        self.assertEqual(2, self.question2.get_weight())
        self.assertEqual(3, self.question3.get_weight())
        # special
        self.assertEqual(0, self.question4.get_weight())
        self.assertEqual(None, self.question5.get_weight())

    # Test add_choice
    def test11_add_choice(self):
        # add choices
        self.question1.add_choice("F")
        self.question2.add_choice("6")

        # special
        self.question1.add_choice("")
        self.question2.add_choice(None)

        # test choice num
        self.assertEqual(6, len(self.question1.choices))
        self.assertEqual(6, len(self.question2.choices))

        # test choices
        self.assertEqual(["A", "B", "C", "D", "E", "F"], self.question1.choices)
        self.assertEqual(["1", "2", "3", "4", "5", "6"], self.question2.choices)

    # test delete_choice
    def test12_delete_choice(self):
        # delete choices
        self.question1.delete_choice(1)
        self.question2.delete_choice(0)

        # special
        self.question1.delete_choice(20)
        self.question2.delete_choice(-1)

        # test choice num
        self.assertEqual(4, len(self.question1.choices))
        self.assertEqual(4, len(self.question2.choices))

        # test choices
        self.assertEqual(["A", "C", "D", "E"], self.question1.choices)
        self.assertEqual(["2", "3", "4", "5"], self.question2.choices)

    # test get_question_type
    def test13_get_question_type(self):
        self.assertEqual("multiple", self.question1.get_question_type())
        self.assertEqual("multiple", self.question2.get_question_type())
        self.assertEqual("multiple", self.question3.get_question_type())
        self.assertEqual("multiple", self.question4.get_question_type())
        self.assertEqual("multiple", self.question5.get_question_type())

    # test get_choice_size
    def test14_get_choice_size(self):
        self.assertEqual(5, self.question1.get_choice_size())
        self.assertEqual(5, self.question2.get_choice_size())
        self.assertEqual(4, self.question3.get_choice_size())
        # special
        self.assertEqual(0, self.question4.get_choice_size())
        self.assertEqual(0, self.question5.get_choice_size())

    # test get_max_num_of_choices
    def test15_get_max_num_of_choices(self):
        self.assertEqual(2, self.question1.get_max_num_of_choice())
        self.assertEqual(3, self.question2.get_max_num_of_choice())
        self.assertEqual(4, self.question3.get_max_num_of_choice())
        # special
        self.assertEqual(2, self.question4.get_max_num_of_choice())
        self.assertEqual(2, self.question5.get_max_num_of_choice())

    # test get_all_choices
    def test16_get_all_choices(self):
        self.assertEqual(["A", "B", "C", "D", "E"], self.question1.get_all_choices())
        self.assertEqual(["1", "2", "3", "4", "5"], self.question2.get_all_choices())
        self.assertEqual(["Python", "Java", "C", "C++"], self.question3.get_all_choices())
        # special
        self.assertEqual([], self.question4.get_all_choices())
        self.assertEqual([], self.question5.get_all_choices())


if __name__ == '__main__':
    unittest.main()
