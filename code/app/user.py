"""
Data structure for user
"""
from abc import ABC, abstractmethod
from code.app.answer_sheet import AnswerSheet


class User(ABC):
    """
    abstract class for user
    """

    def __init__(self, user_id, name, email):
        """

        :param name: the name of the user
        """
        self.id = user_id  # should be unique
        self.name = name
        self.email = email



class Student(User):
    """
    student class
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.response = {}  # record the response from the survey, i.e. {survey id: answer sheet obj}

    def answer_survey(self, survey, raw_answers):
        """
        use this method for the student to answer the survey
        :param survey: survey obj
        :param raw_answers: the answer from the student, in dictionary format {}
        :return: None
        """

        # the response answer sheet
        response_answer_sheet = AnswerSheet(survey=survey)
        # set the response for the answer sheet
        response_answer_sheet.set_answers(raw_answers=raw_answers)
        # put the answer sheet to the student response
        self.response[survey.id] = response_answer_sheet
        # add the student to the survey

        return None

    def get_answer_sheet_by_survey(self,survey):
        """

        @param survey: the survey
        @return: the answer sheet by the survey
        """
        survey_id = survey.id
        return self.response[survey_id]


class Instructor(User):
    """
    Instructor class
    """
    pass
