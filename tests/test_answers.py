import unittest
from code.app import question
from code.app import survey
from code.app import answer


# test single choice answer
class test_single(unittest.TestCase):
    # set up test objects
    def setUp(self):
        self.question1 = question.SingleChoiceQuestion(question_name="q1", description="test q1", weight=1,
                                                       choices=["A", "B", "C"])
        self.question2 = question.SingleChoiceQuestion(question_name="q2", description="test q2", weight=2,
                                                       choices=["1", "2", "3"])
        self.question3 = question.SingleChoiceQuestion(question_name="q3", description="test q3", weight=3,
                                                       choices=["A", "B", "C"])

        self.questions_array1 = [self.question1, self.question2, self.question3]

        self.students1 = ["a", "b", "c"]

        self.survey1 = survey.Survey("survey 1", "s1", self.questions_array1, self.students1)

        self.single1 = answer.SingleChoiceAnswer(question=self.question1, survey=self.survey1, choice_result=0)
        self.single2 = answer.SingleChoiceAnswer(question=self.question2, survey=self.survey1, choice_result=1)
        self.single3 = answer.SingleChoiceAnswer(question=self.question3, survey=self.survey1, choice_result=2)

        # special condition
        self.single4 = answer.SingleChoiceAnswer(question=None, survey=None, choice_result=99999)
        self.single5 = answer.SingleChoiceAnswer(question=None, survey=None, choice_result=-1)
        self.single6 = answer.SingleChoiceAnswer(question=None, survey=None, choice_result=None)

    # test init
    def test01_init(self):
        # test question
        self.assertEqual(self.question1, self.single1.question)
        self.assertEqual(self.question2, self.single2.question)
        self.assertEqual(self.question3, self.single3.question)
        self.assertEqual(None, self.single4.question)
        self.assertEqual(None, self.single5.question)
        self.assertEqual(None, self.single6.question)

        # test survey
        self.assertEqual(self.survey1, self.single1.survey)
        self.assertEqual(self.survey1, self.single2.survey)
        self.assertEqual(self.survey1, self.single3.survey)
        self.assertEqual(None, self.single4.survey)
        self.assertEqual(None, self.single5.survey)
        self.assertEqual(None, self.single6.survey)

        # test choice result
        self.assertEqual(0, self.single1.choice_result)
        self.assertEqual(1, self.single2.choice_result)
        self.assertEqual(2, self.single3.choice_result)
        self.assertEqual(99999, self.single4.choice_result)
        self.assertEqual(-1, self.single5.choice_result)
        self.assertEqual(None, self.single6.choice_result)

        # test question types
        self.assertEqual("single", self.single1.question_type)
        self.assertEqual("single", self.single2.question_type)
        self.assertEqual("single", self.single3.question_type)
        self.assertEqual(None, self.single4.question_type)
        self.assertEqual(None, self.single5.question_type)
        self.assertEqual(None, self.single6.question_type)

        # test answer types
        self.assertEqual("single", self.single1.answer_type)
        self.assertEqual("single", self.single2.answer_type)
        self.assertEqual("single", self.single3.answer_type)
        self.assertEqual("single", self.single4.answer_type)
        self.assertEqual("single", self.single5.answer_type)
        self.assertEqual("single", self.single6.answer_type)

        # test type
        self.assertIsInstance(self.single1, answer.SingleChoiceAnswer)
        self.assertIsInstance(self.single2, answer.SingleChoiceAnswer)
        self.assertIsInstance(self.single3, answer.SingleChoiceAnswer)
        self.assertIsInstance(self.single4, answer.SingleChoiceAnswer)
        self.assertIsInstance(self.single5, answer.SingleChoiceAnswer)
        self.assertIsInstance(self.single6, answer.SingleChoiceAnswer)

    # test get_choice_result
    def test02_get_choice_result(self):
        self.assertEqual(0, self.single1.get_choice_result())
        self.assertEqual(1, self.single2.get_choice_result())
        self.assertEqual(2, self.single3.get_choice_result())
        self.assertEqual(99999, self.single4.get_choice_result())
        self.assertEqual(-1, self.single5.get_choice_result())
        self.assertEqual(None, self.single6.get_choice_result())


# test multiple choice answer
class test_multiple(unittest.TestCase):
    # set up test objects
    def setUp(self):
        self.question4 = question.MultipleChoiceQuestion(question_name="q4", description="test q4", weight=1,
                                                         choices=["A", "B", "C", "D", "E"], max_num_choice=2)
        self.question5 = question.MultipleChoiceQuestion(question_name="q5", description="test q5", weight=2,
                                                         choices=["1", "2", "3", "4", "5"], max_num_choice=3)
        self.question6 = question.MultipleChoiceQuestion(question_name="q6", description="test q6", weight=3,
                                                         choices=["Python", "Java", "C", "C++"], max_num_choice=4)

        self.questions_array2 = [self.question4, self.question5, self.question6]

        self.students2 = ["d", "c", "e", "f"]

        self.survey2 = survey.Survey("survey 2", "s2", self.questions_array2, self.students2)

        self.multiple1 = answer.MultipleChoiceAnswer(question=self.question4, survey=self.survey2,
                                                     choice_result={0: 1, 1: 2})
        self.multiple2 = answer.MultipleChoiceAnswer(question=self.question5, survey=self.survey2,
                                                     choice_result={0: 3, 1: 1, 2: 4})
        self.multiple2 = answer.MultipleChoiceAnswer(question=self.question6, survey=self.survey2,
                                                     choice_result={0: 1, 1: 0, 2: 3, 3: 4})


if __name__ == '__main__':
    unittest.main()
