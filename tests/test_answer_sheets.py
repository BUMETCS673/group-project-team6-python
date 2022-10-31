import unittest
from code.app import question
from code.app import survey
from code.app import answer
from code.app import answer_sheet


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
                                                     choices_result={0: 1, 1: 2})
        self.multiple2 = answer.MultipleChoiceAnswer(question=self.question5, survey=self.survey2,
                                                     choices_result={0: 3, 1: 1, 2: 4})
        self.multiple3 = answer.MultipleChoiceAnswer(question=self.question6, survey=self.survey2,
                                                     choices_result={0: 1, 1: 0, 2: 3, 3: 4})

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
                    self.assertEqual(right_result1[key].choices_result, response.choices_result)

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
                    self.assertEqual(right_result2[key].choices_result, response.choices_result)


if __name__ == '__main__':
    unittest.main()
