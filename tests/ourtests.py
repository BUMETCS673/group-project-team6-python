import unittest
from code.app import team
from code.app import question
from code.app import survey
from code.app import answer_sheet
from code.app import instance
from code.app import answer
from code.app import user





# test survey, not finished
class survey_test(unittest.TestCase):
    # set up test objects
    def setUp(self):
        self.question1 = question.Question("q1", "test q1", 1)
        self.question2 = question.Question("q2", "test q2", 1)
        self.questions1 = [self.question1]
        self.students1 = ["a", "b", "c"]
        self.survey1 = survey.Survey("survey 1", "1", self.questions1, self.students1)

    # test initial function in survey
    def test_survey_init(self):
        # test survey_name
        self.assertEqual(self.survey1.survey_name, "survey 1")

        # test questions
        self.assertEqual(self.survey1.questions[0], self.question1)

        # test students
        self.assertEqual(self.survey1.students, self.students1)

        # test type
        self.assertTrue(isinstance(self.survey1, survey.Survey))

    # test append_question in survey
    def test_append_question(self):
        # add a question
        self.survey1.append_question(self.question2)

        # check num_question
        self.assertEqual(self.survey1.num_question, 2)

        # check questions
        self.assertEqual(self.survey1.questions[1], self.question2)

    # test append_insert_question in survey, not finished
    def test_insert_question(self):
        self.assertEqual(1, 1)

    # test get_all_question_indexes_by_type in survey, not finished
    def get_all_question_indexes_by_type(self):
        self.assertEqual(1, 1)


# test answer, not finished
class answer_test(unittest.TestCase):
    # Set Uo test objects
    def setUp(self):
        self.question1 = question.Question("q1", "test q1", 1)

    def test(self):
        self.assertEqual(1, 1)


# test answer_sheet, not finished
class answer_sheet_test(unittest.TestCase):
    def test(self):
        self.assertEqual(1, 1)


# test team, not finished
class team_test(unittest.TestCase):

    # set up test objects
    def setUp(self):
        self.question1 = question.Question("q1", "test q1", 1)
        self.questions1 = [self.question1]
        self.students1 = ["a", "b", "c"]
        self.survey1 = survey.Survey("s1", "1", self.questions1, self.students1)
        self.team1 = team.Team("team1", self.survey1)

    # test initial function in team
    def test_init(self):
        # test team_name
        self.assertEqual(self.team1.team_name, "team1")

        # test survey_target.survey_name
        self.assertEqual(self.team1.survey_target.survey_name, "s1")

        # test survey_target.questions
        self.assertEqual(self.team1.survey_target.questions, self.questions1)

        # test survey_target.questions
        self.assertEqual(self.team1.survey_target.students, self.students1)

        # test object type
        self.assertTrue(isinstance(self.team1, team.Team))

    # test get_single_choice_scores, not finished
    def test_get_single_choice_scores(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
