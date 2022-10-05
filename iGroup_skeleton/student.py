class Student:

	def __init__(self, student_name,**kwargs):
		# self.student_id = uuid
		self.student_name = student_name
		self.__all_answers = None
		self.survey_answers = None


	@property
	def all_answers(self):
		return self.__all_answers

	@all_answers.deleter
	def all_answers(self):
		del self.__all_answers

