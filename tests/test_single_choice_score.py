import unittest
from source_code.app.score_calculation import single_choice_score


# test single choice score
class test_single_choice_score(unittest.TestCase):
    def setUp(self):
        self.team_size1 = 5
        self.team_size2 = 6
        self.team_size3 = 7

        self.num_choice1 = 3
        self.num_choice2 = 4
        self.num_choice3 = 5

        self.teamsize = [self.team_size1, self.team_size2, self.team_size3]
        self.numchoice = [self.num_choice1, self.num_choice2, self.num_choice3]

        # special
        self.team_size4 = 0
        self.team_size5 = None

    # test cal single score
    def test01_cal_single_score(self):
        for i in self.teamsize:
            for j in self.numchoice:
                answer = j / i
                self.assertEqual(answer, single_choice_score.cal_single_score(i, j))

    # test special condition
    def test02_special(self):
        self.assertEqual(None, single_choice_score.cal_single_score(self.team_size4, 5))

        self.assertEqual(None, single_choice_score.cal_single_score(self.team_size5, 6))

        self.assertEqual(None, single_choice_score.cal_single_score(self.team_size3, None))

    if __name__ == '__main__':
        unittest.main()
