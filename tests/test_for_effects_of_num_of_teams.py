from source_code.app.question import SingleChoiceQuestion, MultipleChoiceQuestion
from source_code.app.survey import Survey
from source_code.app.user import Student
from source_code.app.answer_sheet import AnswerSheet
from source_code.app.team import Team
from source_code.app.instance import Instance
import unittest


# test value weight result
class test_weight(unittest.TestCase):

    def setUp(self):
        self.question_1 = MultipleChoiceQuestion(question_name="q1",
                                                 description="None",
                                                 weight=-1,
                                                 choices=["Java", "C", "Python", "C++", "R", "Ruby"],
                                                 max_num_choice=3)

        self.question_2 = SingleChoiceQuestion(question_name="q2",
                                               description="None",
                                               weight=-1,
                                               choices=["A", "B", "C", "D"])

        self.question_3 = SingleChoiceQuestion(question_name="q3",
                                               description="None",
                                               weight=-1,
                                               choices=["A", "B", "C", "D"])

        self.question_4 = MultipleChoiceQuestion(question_name="q4",
                                                 description="None",
                                                 weight=-1,
                                                 choices=["Java", "C", "Python", "C++", "R", "Ruby"],
                                                 max_num_choice=3)

        self.question_5 = SingleChoiceQuestion(question_name="q5",
                                               description="None",
                                               weight=-1,
                                               choices=["A", "B", "C", "D"])

        self.question_6 = MultipleChoiceQuestion(question_name="q6",
                                                 description="None",
                                                 weight=-1,
                                                 choices=["Java", "C", "Python", "C++", "R", "Ruby"],
                                                 max_num_choice=3)

        student_1 = Student(name="stu 1", email="test@gmail.com", user_id=1)
        student_2 = Student(name="stu 2", email="test@gmail.com", user_id=2)
        student_3 = Student(name="stu 3", email="test@gmail.com", user_id=3)
        student_4 = Student(name="stu 4", email="test@gmail.com", user_id=4)
        student_5 = Student(name="stu 5", email="test@gmail.com", user_id=5)
        student_6 = Student(name="stu 6", email="test@gmail.com", user_id=6)
        student_7 = Student(name="stu 7", email="test@gmail.com", user_id=7)
        student_8 = Student(name="stu 8", email="test@gmail.com", user_id=8)
        student_9 = Student(name="stu 9", email="test@gmail.com", user_id=9)
        student_10 = Student(name="stu 10", email="test@gmail.com", user_id=10)
        student_11 = Student(name="stu 11", email="test@gmail.com", user_id=11)
        student_12 = Student(name="stu 12", email="test@gmail.com", user_id=12)

        self.students_target = [student_1, student_2, student_3, student_4, student_5, student_6, student_7, student_8,
                                student_9, student_10, student_11, student_12]

        questions = [self.question_1, self.question_2, self.question_3,
                     self.question_4, self.question_5, self.question_6]

        student_1_answer = {
            0: {0: 3, 1: 1},  # multiple choice
            1: 0,  # single choice
            2: 1,
            3: {0: 1, 1: 2},
            4: 2,
            5: {0: 2, 1: 1, 2: 3}
        }
        student_2_answer = {
            0: {0: 3, 1: 1},  # multiple choice
            1: 1,  # single choice
            2: 0,
            3: {0: 2, 2: 3},
            4: 2,
            5: {0: 4, 1: 5, 2: 3}
        }
        student_3_answer = {
            0: {0: 3, 1: 2},  # multiple choice
            1: 2,  # single choice
            2: 0,
            3: {0: 3, 2: 4},
            4: 1,
            5: {0: 2, 1: 1, 2: 5}
        }
        student_4_answer = {
            0: {0: 2, 1: 1},  # multiple choice
            1: 0,  # single choice
            2: 1,
            3: {0: 1, 1: 2},
            4: 2,
            5: {0: 1, 1: 2, 2: 3}
        }
        student_5_answer = {
            0: {0: 2, 1: 1},  # multiple choice
            1: 1,  # single choice
            2: 1,
            3: {0: 2, 1: 3},
            4: 3,
            5: {0: 2, 1: 4, 2: 1}
        }
        student_6_answer = {
            0: {0: 2, 1: 1, 2: 4},  # multiple choice
            1: 2,  # single choice
            2: 0,
            3: {0: 3, 1: 4},
            4: 0,
            5: {0: 2, 1: 1, 2: 0}
        }

        student_7_answer = {
            0: {0: 1, 1: 2, 2: 4},  # multiple choice
            1: 0,  # single choice
            2: 2,
            3: {0: 1, 1: 2},
            4: 2,
            5: {0: 0, 1: 1, 2: 3}
        }

        student_8_answer = {
            0: {0: 1, 1: 2},  # multiple choice
            1: 1,  # single choice
            2: 2,
            3: {0: 2, 1: 3},
            4: 3,
            5: {0: 0, 1: 2, 2: 3}
        }

        student_9_answer = {
            0: {0: 1, 1: 3, 2: 4},  # multiple choice
            1: 2,  # single choice
            2: 2,
            3: {0: 3, 1: 4},
            4: 1,
            5: {0: 2, 1: 1, 2: 3}
        }

        student_10_answer = {
            0: {0: 1, 1: 3},  # multiple choice
            1: 2,  # single choice
            2: 3,
            3: {0: 4},
            4: 0,
            5: {0: 1, 1: 2, 2: 5}
        }

        student_11_answer = {
            0: {0: 3, 1: 1},  # multiple choice
            1: 1,  # single choice
            2: 0,
            3: {0: 4, 1: 2},
            4: 1,
            5: {0: 1, 1: 2, 2: 4}
        }

        student_12_answer = {
            0: {0: 1, 1: 2},  # multiple choice
            1: 1,  # single choice
            2: 3,
            3: {0: 4},
            4: 0,
            5: {0: 0, 1: 2, 2: 4}
        }

        self.survey_1 = Survey(survey_name="hello", survey_id="unique_id", questions=questions,
                               students=self.students_target)

        student_1.answer_survey(self.survey_1, student_1_answer)
        student_2.answer_survey(self.survey_1, student_2_answer)
        student_3.answer_survey(self.survey_1, student_3_answer)
        student_4.answer_survey(self.survey_1, student_4_answer)
        student_5.answer_survey(self.survey_1, student_5_answer)
        student_6.answer_survey(self.survey_1, student_6_answer)
        student_7.answer_survey(self.survey_1, student_7_answer)
        student_8.answer_survey(self.survey_1, student_8_answer)
        student_9.answer_survey(self.survey_1, student_9_answer)
        student_10.answer_survey(self.survey_1, student_10_answer)
        student_11.answer_survey(self.survey_1, student_11_answer)
        student_12.answer_survey(self.survey_1, student_12_answer)

    def test01_three_teams(self):
        num_of_team = 3
        test_instance1 = Instance(40, students_target=self.students_target, num_team=num_of_team,
                                  survey_target=self.survey_1)
        num_of_times_running = 20
        flag1 = 0
        for j in range(0, num_of_times_running):
            result = test_instance1.run_instance()
            for i in range(0, num_of_team):
                if result[i].get_total_score() >= test_instance1.scores_after_random_assign[i]:
                    flag1 += 1

        self.assertTrue((flag1 / num_of_times_running) >= 0.8)

    def test02_two_teams(self):
        num_of_team = 2
        test_instance1 = Instance(40, students_target=self.students_target, num_team=num_of_team,
                                  survey_target=self.survey_1)
        num_of_times_running = 20
        flag1 = 0
        for j in range(0, num_of_times_running):
            result = test_instance1.run_instance()
            for i in range(0, num_of_team):
                if result[i].get_total_score() >= test_instance1.scores_after_random_assign[i]:
                    flag1 += 1

        self.assertTrue((flag1 / num_of_times_running) >= 0.8)

    def test03_four_teams(self):
        num_of_team = 4
        test_instance1 = Instance(40, students_target=self.students_target, num_team=num_of_team,
                                  survey_target=self.survey_1)
        num_of_times_running = 20
        flag1 = 0
        for j in range(0, num_of_times_running):
            result = test_instance1.run_instance()
            for i in range(0, num_of_team):
                if result[i].get_total_score() >= test_instance1.scores_after_random_assign[i]:
                    flag1 += 1

        self.assertTrue((flag1 / num_of_times_running) >= 0.8)

