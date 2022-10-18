"""
Data structure for answer class
"""
from abc import ABC, abstractmethod


class Answer(ABC):
    """
    abstract class for the student answer
    """

    def __init__(self, question, survey, **kwargs):
        """

        @param question: the answer corresponding to the question object
        @param survey: the question that in the survey
        @param kwargs: reserved
        """
        self.question_type = question
        self.question_type = question.question_type
        self.survey = survey


class SingleChoiceAnswer(Answer):
    """
    the single choice answer class
    """
    question_types = {
        "single"
    }
    answer_type = "single"

    def __init__(self, choice_result, **kwargs):
        """

        @param choice_result: the choice of student, int: index of the option
        @param kwargs: pass to the super class
        @return: None
        """
        super().__init__(**kwargs)
        self.choice_result = choice_result

    def get_choice_result(self):
        """
        get the choice answer
        @return: the index of the choice
        """
        return self.choice_result


class MultipleChoiceAnswer(Answer):
    """
    the multiple choice answer class
    """
    question_types = {
        "multiple"
    }
    answer_type = "multiple"

    def __init__(self, choices_result, **kwargs):
        """

        @param choices_result: all choices result for the question, should be the dictionary format,
        i.e. {0: 2, 1: 3, 2: 5} which {order of choice, the index of the option}
        @param weights_result: the weights for the choice
        @param kwargs:
        @return:
        """
        super().__init__(**kwargs)
        self.choices_result = choices_result  # should be list, order is the index

        # reserved for future
        # self.weights_result = weights_result

    def get_choice_result(self):
        """
        get the choice answer
        @return: the index of the choice
        """
        return self.choices_result
