from abc import ABC, abstractmethod

class Question(ABC):
	"""abstract class for question"""
	def __init__(self, question_name, description, question_type,weight,**kwargs):
		# self.question_id = uuid
		self.description = description
		self.question_name = question_name
		self.question_type = question_type
		self.weight = weight

class SingleChoiceQuestion(Question):
	"""Single choice question"""
	def __init__(self, choices, **kwargs):
		super().__init__(**kwargs)
		self.choices = choices

