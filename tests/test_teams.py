import unittest
from source_code.app import team
from source_code.app import survey
from source_code.app import question
from source_code.app import user
from source_code.app import answer
from source_code.app import answer_sheet
from source_code.app.score_calculation import multiple_choice_score
from source_code.app.score_calculation import single_choice_score


class test_team1(unittest.TestCase):
    def setUp(self):
        self.question1 = question.SingleChoiceQuestion(question_name="q1", description="test q1", weight=1,
                                                       choices=["A", "B", "C"])
        self.question2 = question.SingleChoiceQuestion(question_name="q2", description="test q2", weight=2,
                                                       choices=["1", "2", "3"])
        self.question3 = question.MultipleChoiceQuestion(question_name="q4", description="test q3", weight=1,
                                                         choices=["A", "B", "C", "D", "E"], max_num_choice=2)
        self.question4 = question.MultipleChoiceQuestion(question_name="q4", description="test q4", weight=2,
                                                         choices=["1", "2", "3", "4", "5"], max_num_choice=3)

        self.student1 = user.Student(user_id="001", name="Jessie", email="jessie@doe.com")
        self.student2 = user.Student(user_id="002", name="James", email="james@doe.com")
        self.student3 = user.Student(user_id="003", name="jack", email="jack@doe.com")

        self.students = [self.student1, self.student2, self.student3]
        self.questions_array = [self.question1, self.question2, self.question3, self.question4]

        self.survey1 = survey.Survey("survey 1", "s1", self.questions_array, self.students)

        self.single1_Jessie = answer.SingleChoiceAnswer(question=self.question1, survey=self.survey1, choice_result=0)
        self.single1_James = answer.SingleChoiceAnswer(question=self.question1, survey=self.survey1, choice_result=1)
        self.single1_Jack = answer.SingleChoiceAnswer(question=self.question1, survey=self.survey1, choice_result=0)

        self.single2_Jessie = answer.SingleChoiceAnswer(question=self.question2, survey=self.survey1, choice_result=1)
        self.single2_James = answer.SingleChoiceAnswer(question=self.question2, survey=self.survey1, choice_result=2)
        self.single2_Jack = answer.SingleChoiceAnswer(question=self.question2, survey=self.survey1, choice_result=3)

        self.multiple1_Jessie = answer.MultipleChoiceAnswer(question=self.question3, survey=self.survey1,
                                                            choices_result=[1, 2])
        self.multiple1_James = answer.MultipleChoiceAnswer(question=self.question3, survey=self.survey1,
                                                           choices_result=[2, 3])
        self.multiple1_Jack = answer.MultipleChoiceAnswer(question=self.question3, survey=self.survey1,
                                                          choices_result=[3, 1])

        self.multiple2_Jessie = answer.MultipleChoiceAnswer(question=self.question4, survey=self.survey1,
                                                            choices_result=[1, 3, 2])
        self.multiple2_James = answer.MultipleChoiceAnswer(question=self.question4, survey=self.survey1,
                                                           choices_result=[2, 3, 4])
        self.multiple2_Jack = answer.MultipleChoiceAnswer(question=self.question4, survey=self.survey1,
                                                          choices_result=[1, 2, 4])

        self.raw_answers_Jessie = {0: 0, 1: 1, 2: {0: 1, 1: 2}, 3: {0: 1, 1: 3, 2: 2}}
        self.raw_answers_James = {0: 1, 1: 2, 2: {0: 2, 1: 3}, 3: {0: 2, 1: 3, 2: 4}}
        self.raw_answers_Jack = {0: 0, 1: 3, 2: {0: 3, 1: 1}, 3: {0: 1, 1: 2, 2: 4}}

        self.student1.answer_survey(survey=self.survey1, raw_answers=self.raw_answers_Jessie)
        self.student2.answer_survey(survey=self.survey1, raw_answers=self.raw_answers_James)
        self.student3.answer_survey(survey=self.survey1, raw_answers=self.raw_answers_Jack)

        self.team1 = team.Team(team_name="t1", survey_target=self.survey1)
        self.team1.team_members = self.students

    # test init
    def test01_init(self):
        self.assertEqual("t1", self.team1.team_name)

        self.assertEqual(self.survey1, self.team1.survey_target)

        for i in self.students:
            self.assertIn(i, self.team1.team_members)

        self.assertEqual(3, self.team1.team_size)

        self.assertIsInstance(self.team1, team.Team)

    # test get single choice
    def test02_get_single_choice_answer(self):
        single_answers = self.team1.get_single_choice_answer()

        for i in self.students:
            if i.id in single_answers.keys():
                self.assertEqual(i.get_answer_sheet_by_survey(survey=self.survey1).
                                 get_all_answers_by_question_type(question_type="single"), single_answers[i.id])

    # test get multiple choice
    def test03_get_multiple_choice_answer(self):
        multiple_answers = self.team1.get_multiple_choice_answer()

        for i in self.students:
            if i.id in multiple_answers.keys():
                self.assertEqual(i.get_answer_sheet_by_survey(survey=self.survey1).
                                 get_all_answers_by_question_type(question_type="multiple"), multiple_answers[i.id])

    # test single score
    def test04_get_single_choice_scores(self):
        single_choice_answers = {"001": self.student1.get_answer_sheet_by_survey(survey=self.survey1).
        get_all_answers_by_question_type(question_type="single"),
                                 "002": self.student2.get_answer_sheet_by_survey(survey=self.survey1).
                                 get_all_answers_by_question_type(question_type="single"),
                                 "003": self.student3.get_answer_sheet_by_survey(survey=self.survey1).
                                 get_all_answers_by_question_type(question_type="single")}

        single_choice_questions_weight = {0: 1, 1: 2}

        scores = {0: 0, 1: 0}

        unique_choice1 = set()
        student_answer1 = single_choice_answers["001"][0]
        student_choice1 = student_answer1.get_choice_result()
        student_answer2 = single_choice_answers["002"][0]
        student_choice2 = student_answer2.get_choice_result()
        student_answer3 = single_choice_answers["003"][0]
        student_choice3 = student_answer3.get_choice_result()

        unique_choice1.add(student_choice1)
        unique_choice1.add(student_choice2)
        unique_choice1.add(student_choice3)
        num_unique_choice1 = len(unique_choice1)

        score1 = single_choice_score.cal_single_score(team_size=3, num_unique_choice=num_unique_choice1)
        scores[0] += score1 * single_choice_questions_weight[0]

        unique_choice2 = set()
        student_answer4 = single_choice_answers["001"][1]
        student_choice4 = student_answer4.get_choice_result()
        student_answer5 = single_choice_answers["002"][1]
        student_choice5 = student_answer5.get_choice_result()
        student_answer6 = single_choice_answers["003"][1]
        student_choice6 = student_answer6.get_choice_result()

        unique_choice2.add(student_choice4)
        unique_choice2.add(student_choice5)
        unique_choice2.add(student_choice6)
        num_unique_choice2 = len(unique_choice2)

        score2 = single_choice_score.cal_single_score(team_size=3, num_unique_choice=num_unique_choice2)
        scores[1] += score2 * single_choice_questions_weight[1]

        self.assertEqual(0.66667, round(self.team1.get_single_choice_scores()[0], 5))
        self.assertEqual(2.0, round(self.team1.get_single_choice_scores()[1], 5))

    # test multiple score
    def test05_get_multiple_choice_scores(self):
        max_valid_choices = 3

        scores = {2: 0, 3: 0}

        max_num_choice1 = min(self.question3.max_num_choice, max_valid_choices)
        option_scores1 = [[0 for _ in range(2)] for _ in range(5)]

        choice_weight1 = max_num_choice1 - 0
        option_scores1[1][0] += choice_weight1
        option_scores1[1][1] += 1
        choice_weight2 = max_num_choice1 - 1
        option_scores1[2][0] += choice_weight2
        option_scores1[2][1] += 1
        choice_weight3 = max_num_choice1 - 0
        option_scores1[2][0] += choice_weight3
        option_scores1[2][1] += 1
        choice_weight4 = max_num_choice1 - 1
        option_scores1[3][0] += choice_weight4
        option_scores1[3][1] += 1
        choice_weight5 = max_num_choice1 - 0
        option_scores1[3][0] += choice_weight5
        option_scores1[3][1] += 1
        choice_weight6 = max_num_choice1 - 1
        option_scores1[1][0] += choice_weight6
        option_scores1[1][1] += 1

        score1 = multiple_choice_score.cal_multiple_score(team_size=3, max_num_choice=2,
                                                          option_scores=option_scores1)
        scores[2] = score1 * self.question3.get_weight()

        max_num_choice2 = min(self.question4.max_num_choice, max_valid_choices)
        option_scores2 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

        choice_weight_a = max_num_choice2 - 0
        option_scores2[1][0] += choice_weight_a
        option_scores2[1][1] += 1
        choice_weight_b = max_num_choice2 - 1
        option_scores2[3][0] += choice_weight_b
        option_scores2[3][1] += 1
        choice_weight_c = max_num_choice2 - 2
        option_scores2[2][0] += choice_weight_c
        option_scores2[2][1] += 1
        choice_weight_d = max_num_choice2 - 0
        option_scores2[2][0] += choice_weight_d
        option_scores2[2][1] += 1
        choice_weight_e = max_num_choice2 - 1
        option_scores2[3][0] += choice_weight_e
        option_scores2[3][1] += 1
        choice_weight_f = max_num_choice2 - 2
        option_scores2[4][0] += choice_weight_f
        option_scores2[4][1] += 1
        choice_weight_g = max_num_choice2 - 0
        option_scores2[1][0] += choice_weight_g
        option_scores2[1][1] += 1
        choice_weight_h = max_num_choice2 - 1
        option_scores2[2][0] += choice_weight_h
        option_scores2[2][1] += 1
        choice_weight_i = max_num_choice2 - 2
        option_scores2[4][0] += choice_weight_i
        option_scores2[4][1] += 1

        score2 = multiple_choice_score.cal_multiple_score(team_size=3, max_num_choice=3,
                                                          option_scores=option_scores2)
        scores[3] = score2 * self.question4.get_weight()

        self.assertEqual({2: 0.4, 3: 0.54}, self.team1.get_mul_choices_scores())

    def test06_get_total_score_by_type(self):
        self.assertEqual(0.94, self.team1.get_total_score_by_type("multiple"))
        self.assertEqual(2.66667, self.team1.get_total_score_by_type("single"))

    def test07_get_total_score(self):
        self.assertEqual(3.60667, self.team1.get_total_score())


if __name__ == '__main__':
    unittest.main()
