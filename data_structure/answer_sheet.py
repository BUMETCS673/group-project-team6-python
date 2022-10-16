"""
Data structure for student
"""
from data_structure.question import SingleChoiceQuestion, MultipleChoiceQuestion


class AnswerSheet:
    """
    Answer sheet class
    Each answer sheet record the response from a student to the survey
    """

    def __init__(self, survey):
        """

        :param survey: the response to the survey object
        """
        self.survey = survey
        self.answer = {}

    def set_answers(self, answers):
        """
        set
        :param answers: the answer to the survey, in dictionary format,
         for example: {question obj : [option_index]}
        :return: None
        """
        # need to add the ability of checking errors
        self.answer = answers
        return None

    def get_single_choice_answer(self):
        """
        get the single choice answer from the answer sheet
        :return: {single choice question : [choice]}
        """
        result = {}
        # find all the answer that has single choice question type
        for question, answer in self.answer.items():
            # check if this question is single choice question type
            if isinstance(question, SingleChoiceQuestion):
                result[question] = answer

        return result

    def get_multiple_choice_answer(self):
        """
        get the multiple choice answer from the answer sheet
        :return: {multiple choice question : [choices,..]}
        """
        result = {}
        # find all the answer that has single choice question type
        for question, answer in self.answer.items():
            # check if this question is single choice question type
            if isinstance(question, MultipleChoiceQuestion):
                result[question] = answer

        return result
