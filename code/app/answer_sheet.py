"""
Data structure for student
"""
from question import SingleChoiceQuestion, MultipleChoiceQuestion
from answer import SingleChoiceAnswer, MultipleChoiceAnswer


class AnswerSheet:
    """
    Answer sheet class, to answer survey, each student need to create an answer sheet
    Each answer sheet record the response from a student to the survey
    """

    def __init__(self, survey):
        """
        one answer sheet correspond to one survey.
        :param survey: the response to the survey object
        """
        self.survey = survey
        self.answers = {}  # key: survey question index, answer object

    def set_answers(self, raw_answers):
        """
        translate the raw input answer from student in json form to the answer sheet.
        :param raw_answers: dict, the answer to the survey in json format
         for example: {question index : answer object}
        :return: None
        """
        for question_index, response in raw_answers.items():
            # get question type
            question = self.survey.get_question_by_index(question_index)
            question_type = question.question_type
            if question_type == "single":
                answer = SingleChoiceAnswer(question=question,
                                            survey=self.survey,
                                            choice_result=response)
            elif question_type == "multiple":
                # need to preprocess the result
                new_response = [val for _, val in sorted(response.items())]
                answer = MultipleChoiceAnswer(question=question,
                                              survey=self.survey,
                                              choices_result=new_response)
                # weights_result=response.values()) reserved for future
            else:
                return False

            # add question to the answers dictionary
            self.answers[question_index] = answer

        return None

    def get_answer_by_index(self, index):
        """
		get answer by the answer index
		@return: the answer obj
		"""
        return self.answers[index]

    def get_all_answer_indexes_by_question_type(self, question_type):
        """
		get all answers' index that belong to such question type
		@param question_type: the question type
		@return: set of indexes
		"""
        result = set()
        for question_idx, answer in self.answers.items():
            if question_type == self.survey.get_question_type_by_index(question_idx):
                result.add(question_idx)

        return result

    def get_all_answers_by_question_type(self, question_type):
        """
		get all answers that belong to such question type
		@param question_type: the question type
		@return: {question index, answer obj}
		"""
        result = dict()
        question_indexes = self.get_all_answer_indexes_by_question_type(question_type=question_type)
        for index in question_indexes:
            result[index] = self.answers[index]

        return result
