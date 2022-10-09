"""
Data structure for user
"""
from abc import ABC, abstractmethod
from answer_sheet import AnswerSheet


class User(ABC):
    """
    abstract class for user
    """

    def __init__(self, name, email):
        """

        :param name: the name of the user
        """
        self.name = name
        self.email = email


class Student(User):
    """
    student class
    """

    def __init__(self, name, email):
        super().__init__(name, email)
        self.response = {}  # record the response from the survey, i.e. {survey obj:{question obj: [choice/choices]}}

    def answer_survey(self, survey, answer):
        """
        use this method for the student to answer the survey
        :param survey: survey obj
        :param answer: the answer from the student, in dictionary format {}
        :return: None
        """

        # the response answer sheet
        response_answer_sheet = AnswerSheet(survey=survey)
        # set the response for the answer sheet
        response_answer_sheet.set_answers(answers=answer)
        # put the answer sheet to the student response
        self.response[survey] = response_answer_sheet

        return None

    pass


class Instructor(User):
    """
    Instructor class
    """
    pass
