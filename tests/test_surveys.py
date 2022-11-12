import unittest
from source_code.app import question
from source_code.app import survey


class survey_test(unittest.TestCase):
    # set up test objects
    def setUp(self):
        self.question1 = question.SingleChoiceQuestion(question_name="q1", description="test q1", weight=1,
                                                       choices=["A", "B", "C"])
        self.question2 = question.SingleChoiceQuestion(question_name="q2", description="test q2", weight=2,
                                                       choices=["1", "2", "3"])
        self.question3 = question.SingleChoiceQuestion(question_name="q3", description="test q3", weight=3,
                                                       choices=["A", "B", "C"])

        self.question4 = question.MultipleChoiceQuestion(question_name="q4", description="test q4", weight=1,
                                                         choices=["A", "B", "C", "D", "E"], max_num_choice=2)
        self.question5 = question.MultipleChoiceQuestion(question_name="q5", description="test q5", weight=2,
                                                         choices=["1", "2", "3", "4", "5"], max_num_choice=3)
        self.question6 = question.MultipleChoiceQuestion(question_name="q6", description="test q6", weight=3,
                                                         choices=["Python", "Java", "C", "C++"], max_num_choice=4)

        self.questions_array1 = [self.question1, self.question2, self.question4]
        self.questions_array2 = [self.question3, self.question5, self.question6]

        self.students1 = ["a", "b", "c"]
        self.students2 = ["d", "c", "e", "f"]

        self.survey1 = survey.Survey("survey 1", "s1", self.questions_array1, self.students1)
        self.survey2 = survey.Survey("survey 2", "s2", self.questions_array2, self.students2)
        # special condition
        self.useless = survey.Survey("", "", None, None)

    # test initial function in survey
    def test01_survey_init(self):
        # test survey_name
        self.assertEqual("survey 1", self.survey1.survey_name)
        self.assertEqual("survey 2", self.survey2.survey_name)
        self.assertEqual("", self.useless.survey_name)

        # test survey_id
        self.assertEqual("s1", self.survey1.id)
        self.assertEqual("s2", self.survey2.id)
        self.assertEqual("", self.useless.id)

        # test questions
        for i in self.survey1.questions:
            self.assertIn(i, self.questions_array1)

        for j in self.survey2.questions:
            self.assertIn(j, self.questions_array2)

        self.assertEqual([], self.useless.questions)

        # test students
        for x in self.survey1.students:
            self.assertIn(x, self.students1)

        for y in self.survey2.students:
            self.assertIn(y, self.students2)

        self.assertEqual([], self.useless.students)

        # test type
        self.assertIsInstance(self.survey1, survey.Survey)
        self.assertIsInstance(self.survey2, survey.Survey)
        self.assertIsInstance(self.useless, survey.Survey)

    # test append_question in survey
    def test02_append_question(self):
        # create questions need to append
        self.question7 = question.SingleChoiceQuestion(question_name="q7", description="test q3", weight=3,
                                                       choices=["A", "B", "C", "D"])

        self.question8 = question.MultipleChoiceQuestion(question_name="q8", description="test q3", weight=3,
                                                         choices=["A", "B", "C", "D"], max_num_choice=2)
        # append questions
        self.survey1.append_question(self.question8)
        self.survey2.append_question(self.question7)

        # check num_question
        self.assertEqual(4, self.survey1.num_question)
        self.assertEqual(4, self.survey2.num_question)

        # check questions after append
        self.assertEqual(self.question8, self.survey1.questions[3])
        self.assertEqual(self.question7, self.survey2.questions[3])

    # test insert_question in survey
    def test03_insert_question(self):
        # create questions need to insert
        self.question7 = question.SingleChoiceQuestion(question_name="q7", description="test q3", weight=3,
                                                       choices=["A", "B", "C", "D"])
        self.question8 = question.MultipleChoiceQuestion(question_name="q8", description="test q3", weight=3,
                                                         choices=["A", "B", "C", "D"], max_num_choice=2)

        # insert questions
        self.survey1.insert_question(2, self.question8)
        self.survey2.insert_question(1, self.question7)
        self.useless.insert_question(0, self.question7)

        # check num_question
        self.assertEqual(4, self.survey1.num_question)
        self.assertEqual(4, self.survey2.num_question)
        self.assertEqual(1, self.useless.num_question)

        # check questions after insert
        self.assertEqual(self.question4, self.survey1.questions[3])
        self.assertEqual(self.question8, self.survey1.questions[2])
        self.assertEqual(self.question2, self.survey1.questions[1])

        self.assertEqual(self.question5, self.survey2.questions[2])
        self.assertEqual(self.question7, self.survey2.questions[1])
        self.assertEqual(self.question3, self.survey2.questions[0])

        self.assertEqual(self.question7, self.useless.questions[0])

    # test get_all_question_indexes_by_type in survey, not finished
    def test04_get_all_question_indexes_by_type(self):
        self.assertEqual({0, 1}, self.survey1.get_all_question_indexes_by_type("single"))
        self.assertEqual({2}, self.survey1.get_all_question_indexes_by_type("multiple"))

        self.assertEqual({0}, self.survey2.get_all_question_indexes_by_type("single"))
        self.assertEqual({1, 2}, self.survey2.get_all_question_indexes_by_type("multiple"))

        # special condition
        self.assertEqual(set(), self.useless.get_all_question_indexes_by_type("single"))
        self.assertEqual(set(), self.useless.get_all_question_indexes_by_type("multiple"))

    # test get_all_question_weight_by_type
    def test05_get_all_question_weight_by_type(self):
        self.assertEqual({0: 1, 1: 2}, self.survey1.get_all_question_weight_by_type("single"))
        self.assertEqual({2: 1}, self.survey1.get_all_question_weight_by_type("multiple"))

        self.assertEqual({0: 3}, self.survey2.get_all_question_weight_by_type("single"))
        self.assertEqual({1: 2, 2: 3}, self.survey2.get_all_question_weight_by_type("multiple"))

        # special condition
        self.assertEqual(dict(), self.useless.get_all_question_weight_by_type("single"))
        self.assertEqual(dict(), self.useless.get_all_question_weight_by_type("multiple"))

    # test get_question_by_index
    def test06_get_question_by_index(self):
        self.assertEqual(self.question2, self.survey1.get_question_by_index(1))
        self.assertEqual(self.question6, self.survey2.get_question_by_index(2))

        # special condition
        self.assertEqual(None, self.survey2.get_question_by_index(50))
        self.assertEqual(None, self.useless.get_question_by_index(2))

    # test get_question_type_by_index
    def test07_get_question_type_by_index(self):
        self.assertEqual("single", self.survey1.get_question_type_by_index(1))
        self.assertEqual("multiple", self.survey1.get_question_type_by_index(2))

        self.assertEqual("single", self.survey2.get_question_type_by_index(0))
        self.assertEqual("multiple", self.survey2.get_question_type_by_index(2))

        # special condition
        self.assertEqual(None, self.useless.get_question_type_by_index(2))
        self.assertEqual(None, self.survey2.get_question_type_by_index(20))

    # test get_all_questions_by_type
    def test08_get_all_questions_by_type(self):
        self.assertEqual({0: self.question1, 1: self.question2}, self.survey1.get_all_questions_by_type("single"))
        self.assertEqual({2: self.question4}, self.survey1.get_all_questions_by_type("multiple"))

        self.assertEqual({0: self.question3}, self.survey2.get_all_questions_by_type("single"))
        self.assertEqual({1: self.question5, 2: self.question6}, self.survey2.get_all_questions_by_type("multiple"))

        # special condition
        self.assertEqual(dict(), self.useless.get_all_questions_by_type("single"))
        self.assertEqual(dict(), self.useless.get_all_questions_by_type("multiple"))


if __name__ == '__main__':
    unittest.main()
