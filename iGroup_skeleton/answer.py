from abc import ABC, abstractmethod


class Answer(ABC):

	def __init__(self,question,student,question_type,survey,**kwargs):
		# self.answer_id = uuid
		self.question_type = question_type
		self.question_obj = question # question
		self.student_obj = student
		self.survey_obj = survey




class SingleChoiceAnswer(Answer):

	def __init__(self,question,student,question_type,survey, choice,**kwargs):
		super().__init__(question,student,question_type,survey,**kwargs)
		self.choice = choice


