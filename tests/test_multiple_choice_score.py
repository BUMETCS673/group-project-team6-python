import unittest
from source_code.app.score_calculation import multiple_choice_score


class test_multiple_score(unittest.TestCase):
    # set up testing data and objects
    def setUp(self):
        self.team_size1 = 5
        self.team_size2 = 6
        self.team_size3 = 7

        self.max_num1 = 3
        self.max_num2 = 4
        self.max_num3 = 5

        self.scores1 = [[1, 1], [2, 2], [3, 3]]
        self.scores2 = [[1, 2], [2, 2], [4, 2], [3, 2]]
        self.scores3 = [[1, 2], [3, 2], [5, 1], [6, 2], [3, 2]]

    def test01_cal_multiple_score(self):
        self.assertEqual(0.96, multiple_choice_score.cal_multiple_score(self.team_size1, self.max_num1,
                                                                        self.scores1))
        self.assertEqual(0.914, multiple_choice_score.cal_multiple_score(self.team_size1, self.max_num1,
                                                                         self.scores2))
        self.assertEqual(0.843, multiple_choice_score.cal_multiple_score(self.team_size1, self.max_num1,
                                                                         self.scores3))

        self.assertEqual(0.986, multiple_choice_score.cal_multiple_score(self.team_size2, self.max_num2,
                                                                         self.scores1))
        self.assertEqual(0.972, multiple_choice_score.cal_multiple_score(self.team_size2, self.max_num2,
                                                                         self.scores2))
        self.assertEqual(0.949, multiple_choice_score.cal_multiple_score(self.team_size2, self.max_num2,
                                                                         self.scores3))

        self.assertEqual(0.994, multiple_choice_score.cal_multiple_score(self.team_size3, self.max_num3,
                                                                         self.scores1))
        self.assertEqual(0.989, multiple_choice_score.cal_multiple_score(self.team_size3, self.max_num3,
                                                                         self.scores2))
        self.assertEqual(0.979, multiple_choice_score.cal_multiple_score(self.team_size3, self.max_num3,
                                                                         self.scores3))

    def test02_special(self):
        self.assertEqual(1, multiple_choice_score.cal_multiple_score(self.team_size1, self.max_num1,
                                                                     [[0, 0]]))

        self.assertEqual(-9999, multiple_choice_score.cal_multiple_score(0, self.max_num1, self.scores1))

        self.assertEqual(-9999, multiple_choice_score.cal_multiple_score(self.team_size1, 0, self.scores1))

        self.assertEqual(-9999, multiple_choice_score.cal_multiple_score(None, self.max_num3,
                                                                         self.scores3))
        self.assertEqual(-9999, multiple_choice_score.cal_multiple_score(self.team_size3, None,
                                                                         self.scores3))
        self.assertEqual(-9999, multiple_choice_score.cal_multiple_score(self.team_size3, self.max_num3,
                                                                         None))


if __name__ == '__main__':
    unittest.main()
