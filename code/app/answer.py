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
        # check None input
        if question is not None:
            self.question = question
            self.question_type = question.question_type
        else:
            self.question = None
            self.question_type = None
        if survey is not None:
            self.survey = survey
        else:
            self.survey = None


class SingleChoiceAnswer(Answer):
    """
    the single choice answer class
    """
    answer_type = "single"

    def __init__(self, choice_result, **kwargs):
        """

        @param choice_result: the choice of student, int: index of the option
        @param kwargs: pass to the super class
        @return: None
        """
        super().__init__(**kwargs)
        # check if choice_result is None
        if choice_result is not None:
            self.choice_result = choice_result
        else:
            self.choice_result = None
            print("choice_result is None")

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
    answer_type = "multiple"

    def __init__(self, choices_result, **kwargs):
        """

        @param choices_result: all choices result for the question, should be the list,
        i.e. {0: 2, 1: 3, 2: 5} which {order of choice, the index of the option}
        @param weights_result: the weights for the choice
        @param kwargs:
        @return:
        """
        super().__init__(**kwargs)
        # check if choice_result is None
        self.choices_result = choices_result  # should be dict, dict key is the index of question

        # reserved for future
        # self.weights_result = weights_result

    def get_choice_result(self):
        """
        get the choice answer
        @return: the index of the choice
        """
        return self.choices_result
