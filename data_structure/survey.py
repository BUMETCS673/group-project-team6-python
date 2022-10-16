"""
Data structure for survey
"""
from data_structure.question import SingleChoiceQuestion, MultipleChoiceQuestion


class Survey:
    """
    survey class
    """

    def __init__(self, survey_name, questions=None, students=None, **kwargs):
        """

        :param survey_name: the name of the survey
        :param questions: the question in the survey (list type i.e. [question obj])
        :param students: the student that should receive the survey(set type i.e. {student obj})
        :param kwargs: reserved for future use
        """
        # if not default students
        if students is None:
            students = {}

        # if no default questions in the survey
        if questions is None:
            questions = []

        self.survey_name = survey_name
        self.questions = questions
        self.num_question = len(questions)
        self.students = students
        self.num_student = len(students)
        self.send_survey = False
        self.active = False

    def append_question(self, question):
        """
        append question to the last question in the survey
        :param question: the question obj
        :return: None
        """
        # append last element to the questions
        self.questions.append(question)

        # update the num_question
        self.num_question += 1

        return None

    def insert_question(self, index_to_insert, question):
        """

        :param index_to_insert: index to insert the question
        :param question: question obj
        :return: None
        """

        self.questions.insert(index_to_insert, question)

        return None

    def get_all_single_choice_question(self):
        """
        get all the single choice question and its options
        :return: {question obj: [available options]}
        """
        result = {}
        # find all the answer that has single choice question type
        for question in self.questions:
            # check if this question is single choice question type
            if isinstance(question, SingleChoiceQuestion):
                result[question] = question.choices

        return result

    def get_all_single_choice_question_weight(self):
        """
        get all the single choice question weights
        :return: {question obj: weight}
        """
        result = {}
        # find all the answer that has single choice question type
        for question in self.questions:
            # check if this question is single choice question type
            if isinstance(question, SingleChoiceQuestion):
                result[question] = question.weight

        return result


    def get_all_multiple_choice_question(self):
        """

        :return:
        """
        pass
