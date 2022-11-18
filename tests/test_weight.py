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
        self.survey_1 = Survey(survey_name="hello", survey_id="unique_id", questions=None, students=None)

        self.question_1 = MultipleChoiceQuestion(question_name="q1",
                                                 description="None",
                                                 weight=-3,
                                                 choices=["Java", "C", "Python", "C++", "R", "Ruby"],
                                                 max_num_choice=3)

        self.survey_1.append_question(self.question_1)

        student_1 = Student(name="stu 1", email="test@gmail.com", user_id=1)
        student_2 = Student(name="stu 2", email="test@gmail.com", user_id=2)
        student_3 = Student(name="stu 3", email="test@gmail.com", user_id=3)
        student_4 = Student(name="stu 4", email="test@gmail.com", user_id=4)
        student_5 = Student(name="stu 5", email="test@gmail.com", user_id=5)
        student_6 = Student(name="stu 6", email="test@gmail.com", user_id=6)
        student_7 = Student(name="stu 7", email="test@gmail.com", user_id=7)
        student_8 = Student(name="stu 8", email="test@gmail.com", user_id=8)
        student_9 = Student(name="stu 9", email="test@gmail.com", user_id=9)

        student_1_answer = {
            0: {0: 3}  # multiple choice
        }
        student_2_answer = {
            0: {0: 3}  # multiple choice
        }
        student_3_answer = {
            0: {0: 3}  # multiple choice
        }
        student_4_answer = {
            0: {0: 2}  # multiple choice
        }
        student_5_answer = {
            0: {0: 2}  # multiple choice
        }
        student_6_answer = {
            0: {0: 2}  # multiple choice
        }

        student_7_answer = {
            0: {0: 1}  # multiple choice
        }

        student_8_answer = {
            0: {0: 1}  # multiple choice
        }

        student_9_answer = {
            0: {0: 1}  # multiple choice
        }

        student_1.answer_survey(self.survey_1, student_1_answer)
        student_2.answer_survey(self.survey_1, student_2_answer)
        student_3.answer_survey(self.survey_1, student_3_answer)
        student_4.answer_survey(self.survey_1, student_4_answer)
        student_5.answer_survey(self.survey_1, student_5_answer)
        student_6.answer_survey(self.survey_1, student_6_answer)
        student_7.answer_survey(self.survey_1, student_7_answer)
        student_8.answer_survey(self.survey_1, student_8_answer)
        student_9.answer_survey(self.survey_1, student_9_answer)

        self.students_target = [student_1, student_2, student_3, student_4, student_5, student_6, student_7, student_8,
                                student_9]

    def test01_negative_weight_accuracy(self):
        test_instance = Instance(50, students_target=self.students_target, num_team=3, survey_target=self.survey_1)
        num_of_times_running = 50
        most_accurate = 0
        for i in range(0, num_of_times_running):
            result = test_instance.run_instance()
            if sum(k.get_total_score() for k in result) == 0:
                most_accurate = most_accurate + 1

        self.assertTrue((most_accurate / num_of_times_running) > 0.8)

    def test02_positive_weight_accuracy(self):
        self.survey_1.questions[0].weight = 5
        test_instance = Instance(50, students_target=self.students_target, num_team=3, survey_target=self.survey_1)
        num_of_times_running = 50
        most_accurate = 0
        for i in range(0, num_of_times_running):
            result = test_instance.run_instance()

            if sum(k.get_total_score() for k in result) == 15:
                most_accurate = most_accurate + 1

        self.assertTrue((most_accurate / num_of_times_running) > 0.8)


if __name__ == '__main__':
    unittest.main()
