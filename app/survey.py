"""
Data structure for survey
"""
from question import SingleChoiceQuestion, MultipleChoiceQuestion


class Survey:
	"""
    survey class
    """

	def __init__(self, survey_name, survey_id, questions=None, students=None, **kwargs):
		"""

        :param survey_name: the name of the survey
        :param survey_id: unique survey id
        :param questions: the question in the survey (list type i.e. [question obj])
        :param students: the student that should receive the survey(set type i.e. {student obj})
        :param kwargs: reserved for future use
        """
		# if not default students
		if students is None:
			students = []

		# if no default questions in the survey
		if questions is None:
			questions = []
		self.id = survey_id  # should be unique
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

	def get_all_question_indexes_by_type(self, question_type):
		"""
		get all questions indexes by such question type
		@param question_type: string, type of the question
		@return: the indexes of such type
		"""
		result = set()
		for index, question in enumerate(self.questions):
			if question.question_type == question_type:
				result.add(index)
		return result

	def get_all_question_weight_by_type(self, question_type):
		"""
		get all question by type
		@param question_type:
		@return: {question index, question weight}
		"""
		questions = self.get_all_questions_by_type(question_type=question_type)
		result = dict()
		for index, question in questions.items():
			result[index] = question.get_weight()
		return result

	def get_question_by_index(self, index_value):
		"""
		get the question obj by the index
		@param index_value: the question position in the survey
		@return: the question obj
		"""
		return self.questions[index_value]

	def get_question_type_by_index(self, index_value):
		"""
		get question type by the index value
		@param index_value: the index value of the question
		@return: the type of such question
		"""
		question = self.get_question_by_index(index_value)
		question_type = question.question_type
		return question_type

	def get_all_questions_by_type(self, question_type):
		"""
        get all the such type question and its options
        :return: {question index: question obj}
        """
		result = dict()
		indexes_result = self.get_all_question_indexes_by_type(question_type=question_type)
		# find all the answer that has such question type
		for question_index in indexes_result:
			# check if this question is such question type
			result[question_index] = self.questions[question_index]
		return result
