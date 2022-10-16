import unittest
from data_structure import team
from data_structure import question
from data_structure import survey
from data_structure import answer_sheet as an


# test survey, not finished
class question_test(unittest.TestCase):
    # set up test objects
    def setUp(self):
        self.question1 = question.Question("q1", "test q1", "SingleChoiceQuestion", 1)

    def test_question_init(self):
        # test question_name
        self.assertEqual(self.question1.question_name, "q1")

        # test description
        self.assertEqual(self.question1.description, "test q1")

        # test question_type
        self.assertEqual(self.question1.question_type, "SingleChoiceQuestion")

        # test weight
        self.assertEqual(self.question1.weight, 1)

        # test type
        self.assertTrue(isinstance(self.question1, question.Question))


# test survey, not finished
class survey_test(unittest.TestCase):
    # set up test objects
    def setUp(self):
        self.question1 = question.Question("q1", "test q1", "SingleChoiceQuestion", 1)
        self.questions1 = [self.question1]
        self.students1 = ["a", "b", "c"]
        self.survey1 = survey.Survey("s1", self.questions1, self.students1)

    def test_survey_init(self):
        # test survey_name
        self.assertEqual(self.survey1.survey_name, "s1")

        # test questions
        self.assertEqual(self.survey1.questions, self.questions1)

        # test students
        self.assertEqual(self.survey1.students, self.students1)

        # test type
        self.assertTrue(isinstance(self.survey1, survey.Survey))


# test answer, not finished
class answer_test(unittest.TestCase):
    def test(self):
        self.assertEqual(1, 1)


# test team, not finished
class team_test(unittest.TestCase):

    # set up test objects
    def setUp(self):
        self.question1 = question.Question("q1", "test q1", "SingleChoiceQuestion", 1)
        self.questions1 = [self.question1]
        self.students1 = ["a", "b", "c"]
        self.survey1 = survey.Survey("s1", self.questions1, self.students1)
        self.team1 = team.Team(3, "good", self.survey1)

    # test initial function in team
    def test_init(self):
        # test team_size
        self.assertEqual(self.team1.team_size, 3)

        # test team_name
        self.assertEqual(self.team1.team_name, "good")

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
