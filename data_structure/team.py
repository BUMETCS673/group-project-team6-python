import math


class Team:
    total_score = 0

    def __init__(self, team_size, team_name, survey_target, **kwargs):
        """

        :param team_size: the size of the team
        :param team_name: the name of the team
        :param members: list of students in the team
        :param survey: the survey that is targeting for calculating the team score
        :param kwargs: reserved
        """
        self.team_size = team_size
        self.team_name = team_name
        self.__team_members = None  # list of student
        self.survey_target = survey_target

    @property
    def team_members(self):
        # print(f"show group{self.team_name} members:{self.__team_members}")
        return self.__team_members

    @team_members.setter
    def team_members(self, members):
        print("set team members")
        self.__team_members = members

    @team_members.deleter
    def team_members(self):
        print("deleting all members in the team")
        del self.__team_members

    def add_team_member(self, student):
        self.team_members.append(student)

    def get_team_size(self):
        return len(self.__team_members)

    def get_single_choice_scores(self):
        """
        calculate all the single choice scores for the team
        :return: the score of all single choice questions of all members in the team
        """

        # for each student,
        # get single choice answers in the dictionary format {student id : {question index, answer obj}}
        single_choice_answers = {}
        for student in self.__team_members:
            # do the query, get the student response(answer sheet) to that survey
            student_answer_sheet = student.get_answer_sheet_by_survey(survey=self.survey_target)
            # get the all single choice questions from the student answer sheet, and put it in the
            # single_choice_questions dict
            single_choice_answers[student.id] = student_answer_sheet.get_all_answers_by_question_type(
                question_type="single")
        # get the single choice question in the dictionary format {question index : question obj}
        single_choice_questions = self.survey_target.get_all_questions_by_type(question_type="single")

        # get the single choice question weight in the dictionary format {question index : weight}
        single_choice_questions_weight = self.survey_target.get_all_question_weight_by_type(question_type="single")

        # initialize result dict = {question index, score}
        scores = {question_index: 0 for question_index in single_choice_questions.keys()}

        # the calculation for the score
        # for each single choice question
        for question_index, single_question_obj in single_choice_questions.items():
            unique_choice = set()
            # for each student answer this question
            for student in self.__team_members:
                # print(student.id, single_question)
                student_answer = single_choice_answers[student.id][question_index]
                student_choice = student_answer.get_choice_result()
                unique_choice.add(student_choice)
            # find the total len of unique choice
            unique_len = len(unique_choice)
            scores[question_index] += (unique_len / len(self.__team_members)) * single_choice_questions_weight[
                question_index]

        return scores

    def get_mul_choices_scores(self):
        """
        calculate all multiple choice scores for this team
        @return: all multiple choice question scores for this team.
        """
        self.team_size = len(self.__team_members)

        # for each student, get multiple choice answers in the
        # dictionary format {student id : {question index, multiple choice answer obj}}
        multiple_choice_answers = {}
        for student in self.__team_members:
            # do the query, get the student response(answer sheet) to that survey
            student_answer_sheet = student.get_answer_sheet_by_survey(survey=self.survey_target)
            # get the all multiple choice questions from the student answer sheet, and put it in the
            # multiple_choice_answers dict
            multiple_choice_answers[student.id] = student_answer_sheet.get_all_answers_by_question_type(
                question_type="multiple")

        # get the multiple choice question in the dictionary format {question index : question obj}
        multiple_choice_questions = self.survey_target.get_all_questions_by_type(question_type="multiple")

        # get the multiple choice question weight in the dictionary format {question index : weight}
        multiple_choice_questions_weight = self.survey_target.get_all_question_weight_by_type(question_type="multiple")

        # max valid choices will be the size of this team
        max_valid_choices = len(self.__team_members)

        # initialize result dict = {question index, score}
        scores = {question_index: 0 for question_index in multiple_choice_questions.keys()}

        # the calculation for the score
        # for each multiple question
        for question_index, multiple_question_obj in multiple_choice_questions.items():
            # find max number of choice for each multiple question
            max_choice_num = min(multiple_question_obj.max_num_choice, max_valid_choices)
            # initialize 0 score dict to record each option scores

            # [[0,0]] [score for i option, number of occurrence for ith]
            option_scores = [[0 for _ in range(2)] for _ in range(multiple_question_obj.get_choice_size())]

            # for each student calculate and add the option score to the option_scores
            for student in self.__team_members:
                # get the student multiple choice result
                choice_result = multiple_choice_answers[student.id][question_index].get_choice_result()

                # according to the order, add choices score to the option_scores
                for order, choice_index in enumerate(choice_result):
                    # check if number of choice exceed the max number of choice
                    if order > max_choice_num - 1:
                        break
                    # set choice weight, the larger order the less weight, choice index 0 has weight max_choice_num
                    choice_weight = max_choice_num - order
                    # update option_scores score and occurrence
                    option_scores[choice_index][0] += choice_weight

                    option_scores[choice_index][1] += 1

            # after having option_scores, we can calculate the total scores for this question

            # drop the scores with occurrence less or equal to 1
            option_scores = [score for score in option_scores if score[1] > 1]
            # calculate the total scores

            # 1. need to find the base
            expression = lambda x: x ** 2
            base = (self.team_size ** 2)* sum(expression(max_choice_num - i) for i in range(max_choice_num))
            sum_b = sum(expression(i[0]) for i in option_scores)
            score = 1 - sum_b / base
            # up date scores
            scores[question_index] = score

        return scores

    def get_sch_score(self):
        pass
