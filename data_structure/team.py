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

    def get_single_choice_scores(self):
        """
        calculate all the single choice scores for the team
        :return: the score of all single choice questions of all members in the team
        """

        # for each student,
        # get single choice answers in the dictionary format {student obj : {question obj, [choice]}}
        single_choice_answers = {}
        for student in self.__team_members:
            # do the query, get the student response(answer sheet) to that survey
            student_answer_sheet = student.response[self.survey_target]
            # get the all single choice questions from the student answer sheet, and put it in the single_choice_questions dict
            single_choice_answers[student] = student_answer_sheet.get_single_choice_answer()

        # get the single choice question in the dictionary format {question obj : [available choices]}
        single_choice_questions = self.survey_target.get_all_single_choice_question()

        # get the single choice question in the dictionary format {question obj : weight}
        single_choice_questions_weight = self.survey_target.get_all_single_choice_question_weight()

        # initialize result dict = {question obj , score}
        scores = {question_obj:0 for question_obj in single_choice_questions.keys()}

        # the calculation for the score
        for single_question, available_choices in single_choice_questions.items():
            unique_choice = set()
            for stu in self.__team_members:
                print(stu, single_question)
                student_choice = single_choice_answers[stu][single_question][0]
                unique_choice.add(student_choice)
            unique_len = len(unique_choice)
            scores[single_question] += (unique_len / len(self.__team_members)) * single_choice_questions_weight[
                single_question]

        return scores

    def get_mul_choices_score(self):
        pass

    def get_sch_score(self):
        pass
