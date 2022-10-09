"""
Data structure for question collections
"""
from abc import ABC, abstractmethod


class Question(ABC):
    """
    abstract class for question
    """

    def __init__(self, question_name, description, question_type, weight, **kwargs):
        """

        :param question_name: the name for the question
        :param description: the description for the question
        :param question_type: the type of this question
        :param weight: the weight of this question
        :param kwargs: reserved for future use
        """
        self.description = description
        self.question_name = question_name
        self.question_type = question_type
        self.weight = weight


class SingleChoiceQuestion(Question):
    """
    Single choice question
    """

    def __init__(self, choices=None, **kwargs):
        """

        :param choices: the all available choices in list datatype, default to None
        :param kwargs: reserved for future use
        """
        super().__init__(**kwargs)
        if choices is None:
            choices = []
        self.choices = choices  # should contain list of options

    def add_choice(self, choice):
        """
        Add available option to the question
        :param choice: str datatype, add the available option to the question
        :return: None
        """
        self.choices.append(choice)

        return None

    def delete_choice(self, choice_index):
        """

        :param choice_index: the index of the choice need to be deleted from the question
        :return: None
        """
        pass


class MultipleChoiceQuestion(Question):
    """Multiple choice question"""

    def __init__(self, choices=None, max_num_choice=0, **kwargs):
        """

        :param choices: all available choices in list datatype, default to None
        :param max_num_choice: the max number of choice in int datatype student can choose, default to 0
        :param kwargs: reserved for future use
        """
        super().__init__(**kwargs)
        if choices is None:
            choices = []
        self.choices = choices
        self.max_num_choice = max_num_choice

    def add_choice(self, choice):
        """
        Add available option to the question
        :param choice: str datatype, add the available option to the question
        :return: None
        """
        self.choices.append(choice)

        return None

    def delete_choice(self, choice_index):
        """

        :param choice_index: the index of the choice need to be deleted from the question
        :return: None
        """
        pass
