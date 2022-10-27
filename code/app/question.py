"""
Data structure for question collections
"""
from abc import ABC, abstractmethod


class Question(ABC):
    """
    abstract class for question
    """

    def __init__(self, question_name, description, weight, **kwargs):
        """
        :param question_name: the name for the question
        :param description: the description for the question
        :param weight: the weight of this question
        :param kwargs: reserved for future use
        """
        # check None inputs
        if description is not None:
            self.description = description
        else:
            self.description = None

        if question_name is not None:
            self.question_name = question_name
        else:
            self.question_name = None

        if weight is not None:
            self.weight = weight
        else:
            self.weight = None

    def get_weight(self):
        return self.weight


class SingleChoiceQuestion(Question):
    """
    Single choice question
    """
    question_type = "single"

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
        # check legal new choice
        if choice is not None and choice != "":
            self.choices.append(choice)
        else:
            print("input is illegal")

    def get_question_type(self):
        return self.question_type

    def delete_choice(self, choice_index):
        # check choices len, and choice_index
        if len(self.choices) > 0:
            if len(self.choices) > choice_index >= 0:
                self.choices.pop(choice_index)
            else:
                print("index out of bound")
        else:
            print("choices is empty")
        """
        :param choice_index: the index of the choice need to be deleted from the question
        :return: None
        """

    def get_all_choice(self):
        """
        get all available
        @return: [all available choices]
        """
        return self.choices

    def get_choice_size(self):
        """
        get size of the options
        @return: int of length
        """
        return len(self.choices)


class MultipleChoiceQuestion(Question):
    """Multiple choice question"""
    question_type = "multiple"

    def __init__(self, choices=None, max_num_choice=9999, **kwargs):
        """
        :param choices: all available choices in list datatype, default to None
        :param max_num_choice: the max number of choice in int datatype student can choose, default to 0
        :param choices_score: the scores of each choice
        :param kwargs: reserved for future use
        """
        super().__init__(**kwargs)
        if choices is None:
            choices = []

        self.choices = choices

        if max_num_choice is not None and max_num_choice >= 2:
            self.max_num_choice = max_num_choice
        else:
            self.max_num_choice = 2

    def add_choice(self, choice):
        """
        Add available option to the question
        :param choice: str datatype, add the available option to the question
        :return: None
        """
        # check legal new choice
        if choice is not None and choice != "":
            self.choices.append(choice)
        else:
            print("input is illegal")

    def delete_choice(self, choice_index):
        # check choices len, and choice_index
        if len(self.choices) > 0:
            if len(self.choices) > choice_index >= 0:
                self.choices.pop(choice_index)
            else:
                print("index out bound")
        else:
            print("choices is empty")
        """
        :param choice_index: the index of the choice need to be deleted from the question
        :return: None
        """

    def get_question_type(self):
        return self.question_type

    def get_choice_size(self):
        """
        get size of the options
        @return: int of length
        """
        return len(self.choices)

    def get_max_num_of_choice(self):
        """
        get max number of the options that can be chosen
        @return: int
        """
        return self.max_num_choice

    def get_all_choices(self):
        """
        get all choice in this question
        @return: string array
        """
        return self.choices
