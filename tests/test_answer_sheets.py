import unittest
from source_code.app import question
from source_code.app import survey
from source_code.app import answer
from source_code.app import answer_sheet


# test answer_sheets
class answer_sheets_test(unittest.TestCase):
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
        self.questions_array2 = [self.question5, self.question6, self.question3]

        self.students1 = ["a", "b", "c"]
        self.students2 = ["d", "c", "e", "f"]

        self.survey1 = survey.Survey("survey 1", "s1", self.questions_array1, self.students1)
        self.survey2 = survey.Survey("survey 2", "s2", self.questions_array2, self.students2)

        self.single1 = answer.SingleChoiceAnswer(question=self.question1, survey=self.survey1, choice_result=0)
        self.single2 = answer.SingleChoiceAnswer(question=self.question2, survey=self.survey1, choice_result=1)
        self.single3 = answer.SingleChoiceAnswer(question=self.question3, survey=self.survey1, choice_result=2)

        self.multiple1 = answer.MultipleChoiceAnswer(question=self.question4, survey=self.survey2,
                                                     choices_result=[1, 2])
        self.multiple2 = answer.MultipleChoiceAnswer(question=self.question5, survey=self.survey2,
                                                     choices_result=[3, 1, 4])
        self.multiple3 = answer.MultipleChoiceAnswer(question=self.question6, survey=self.survey2,
                                                     choices_result=[1, 0, 3, 4])

        self.raw_answers1 = {0: self.single1.choice_result, 1: self.single2.choice_result,
                             2: self.multiple1.choices_result}
        self.raw_answers2 = {0: self.multiple2.choices_result, 1: self.multiple3.choices_result,
                             2: self.single3.choice_result}

        self.answer_sheet1 = answer_sheet.AnswerSheet(survey=self.survey1)
        self.answer_sheet2 = answer_sheet.AnswerSheet(survey=self.survey2)

        # special
        self.answer_sheet3 = answer_sheet.AnswerSheet(survey=None)

    # test init
    def test01_init(self):
        # test survey
        self.assertEqual(self.survey1, self.answer_sheet1.survey)
        self.assertEqual(self.survey2, self.answer_sheet2.survey)
        self.assertEqual(None, self.answer_sheet3.survey)

        # test answers
        self.assertEqual(dict(), self.answer_sheet1.answers)
        self.assertEqual(dict(), self.answer_sheet2.answers)
        self.assertEqual(dict(), self.answer_sheet3.answers)

    # test set answers
    def test02_set_answers(self):
        self.answer_sheet1.set_answers(raw_answers=self.raw_answers1)
        self.answer_sheet2.set_answers(raw_answers=self.raw_answers2)

        # special
        self.answer_sheet3.set_answers(raw_answers=self.raw_answers2)
        self.answer_sheet2.set_answers(raw_answers=None)

        right_result1 = {0: self.single1, 1: self.single2, 2: self.multiple1}
        right_result2 = {0: self.multiple2, 1: self.multiple3, 2: self.single3}

        for key, response in self.answer_sheet1.answers.items():
            if key in right_result1.keys():
                self.assertEqual(right_result1[key].question, response.question)
                if right_result1[key].question_type == "single":
                    self.assertEqual(right_result1[key].question_type, response.question_type)
                    self.assertEqual(self.survey1, response.survey)
                    self.assertEqual(right_result1[key].choice_result, response.choice_result)
                else:
                    self.assertEqual(right_result1[key].question_type, response.question_type)
                    self.assertEqual(self.survey1, response.survey)
                    self.assertEqual(sorted(right_result1[key].choices_result), response.choices_result)

        for key, response in self.answer_sheet2.answers.items():
            if key in right_result2.keys():
                self.assertEqual(right_result2[key].question, response.question)
                if right_result2[key].question_type == "single":
                    self.assertEqual(right_result2[key].question_type, response.question_type)
                    self.assertEqual(self.survey2, response.survey)
                    self.assertEqual(right_result2[key].choice_result, response.choice_result)
                else:
                    self.assertEqual(right_result2[key].question_type, response.question_type)
                    self.assertEqual(self.survey2, response.survey)
                    self.assertEqual(sorted(right_result2[key].choices_result), response.choices_result)

        # special
        self.assertEqual(dict(), self.answer_sheet3.answers)

    # test get answer by index
    def test03_get_answer_by_index(self):
        self.answer_sheet1.set_answers(raw_answers=self.raw_answers1)
        self.answer_sheet2.set_answers(raw_answers=self.raw_answers2)

        self.assertEqual(self.single1.choice_result, self.answer_sheet1.get_answer_by_index(0).choice_result)
        self.assertEqual(self.survey1, self.answer_sheet1.get_answer_by_index(0).survey)
        self.assertEqual(self.question1, self.answer_sheet1.get_answer_by_index(0).question)

        self.assertEqual(sorted(self.multiple1.choices_result),
                         self.answer_sheet1.get_answer_by_index(2).choices_result)
        self.assertEqual(self.survey1, self.answer_sheet1.get_answer_by_index(2).survey)
        self.assertEqual(self.question4, self.answer_sheet1.get_answer_by_index(2).question)

        self.assertEqual(sorted(self.multiple2.choices_result),
                         self.answer_sheet2.get_answer_by_index(0).choices_result)
        self.assertEqual(self.survey2, self.answer_sheet2.get_answer_by_index(0).survey)
        self.assertEqual(self.question5, self.answer_sheet2.get_answer_by_index(0).question)

        self.assertEqual(self.single3.choice_result, self.answer_sheet2.get_answer_by_index(2).choice_result)
        self.assertEqual(self.survey2, self.answer_sheet2.get_answer_by_index(2).survey)
        self.assertEqual(self.question3, self.answer_sheet2.get_answer_by_index(2).question)

        # special
        self.assertEqual(None, self.answer_sheet1.get_answer_by_index(1111111))
        self.assertEqual(None, self.answer_sheet2.get_answer_by_index(None))
        self.assertEqual(None, self.answer_sheet3.get_answer_by_index(2))

    # test get all answer indexes by question type
    def test04_get_all_answer_indexes_by_question_type(self):
        self.answer_sheet1.set_answers(raw_answers=self.raw_answers1)
        self.answer_sheet2.set_answers(raw_answers=self.raw_answers2)

        self.assertEqual({0, 1}, self.answer_sheet1.get_all_answer_indexes_by_question_type("single"))
        self.assertEqual({2}, self.answer_sheet2.get_all_answer_indexes_by_question_type("single"))

        self.assertEqual({2}, self.answer_sheet1.get_all_answer_indexes_by_question_type("multiple"))
        self.assertEqual({0, 1}, self.answer_sheet2.get_all_answer_indexes_by_question_type("multiple"))

        # special
        self.assertEqual(set(), self.answer_sheet1.get_all_answer_indexes_by_question_type("simple question"))
        self.assertEqual(set(), self.answer_sheet2.get_all_answer_indexes_by_question_type(None))
        self.assertEqual(set(), self.answer_sheet3.get_all_answer_indexes_by_question_type("single"))

    # test get_all_answers_by_question_type
    def test05_get_all_answers_by_question_type(self):
        self.answer_sheet1.set_answers(raw_answers=self.raw_answers1)
        self.answer_sheet2.set_answers(raw_answers=self.raw_answers2)

        self.assertEqual(self.single1.choice_result,
                         self.answer_sheet1.get_all_answers_by_question_type("single")[0].choice_result)
        self.assertEqual(self.survey1, self.answer_sheet1.get_all_answers_by_question_type("single")[0].survey)
        self.assertEqual(self.question1, self.answer_sheet1.get_all_answers_by_question_type("single")[0].question)

        self.assertEqual(self.single2.choice_result,
                         self.answer_sheet1.get_all_answers_by_question_type("single")[1].choice_result)
        self.assertEqual(self.survey1, self.answer_sheet1.get_all_answers_by_question_type("single")[1].survey)
        self.assertEqual(self.question2, self.answer_sheet1.get_all_answers_by_question_type("single")[1].question)

        self.assertEqual(sorted(self.multiple1.choices_result),
                         self.answer_sheet1.get_all_answers_by_question_type("multiple")[2].choices_result)
        self.assertEqual(self.survey1, self.answer_sheet1.get_all_answers_by_question_type("multiple")[2].survey)
        self.assertEqual(self.question4, self.answer_sheet1.get_all_answers_by_question_type("multiple")[2].question)

        self.assertEqual(sorted(self.multiple2.choices_result),
                         self.answer_sheet2.get_all_answers_by_question_type("multiple")[0].choices_result)
        self.assertEqual(self.survey2, self.answer_sheet2.get_all_answers_by_question_type("multiple")[0].survey)
        self.assertEqual(self.question5, self.answer_sheet2.get_all_answers_by_question_type("multiple")[0].question)

        self.assertEqual(sorted(self.multiple3.choices_result),
                         self.answer_sheet2.get_all_answers_by_question_type("multiple")[1].choices_result)
        self.assertEqual(self.survey2, self.answer_sheet2.get_all_answers_by_question_type("multiple")[1].survey)
        self.assertEqual(self.question6, self.answer_sheet2.get_all_answers_by_question_type("multiple")[1].question)

        self.assertEqual(self.single3.choice_result,
                         self.answer_sheet2.get_all_answers_by_question_type("single")[2].choice_result)
        self.assertEqual(self.survey2, self.answer_sheet2.get_all_answers_by_question_type("single")[2].survey)
        self.assertEqual(self.question3, self.answer_sheet2.get_all_answers_by_question_type("single")[2].question)

        # special
        self.assertEqual(dict(), self.answer_sheet1.get_all_answers_by_question_type("simple answer"))
        self.assertEqual(dict(), self.answer_sheet2.get_all_answers_by_question_type(None))
        self.assertEqual(dict(), self.answer_sheet3.get_all_answers_by_question_type("single"))


if __name__ == '__main__':
    unittest.main()
