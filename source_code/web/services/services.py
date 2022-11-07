"""this includes all the services"""
from .app.survey import Survey
from .app.question import SingleChoiceQuestion, MultipleChoiceQuestion


class iGroupService:
	def __init__(self, instance_config_obj, survey_service_obj, student_service_obj):
		pass


def get_clean_options_from_question(question_obj):
	"""
	clean the object set
	:param question_obj: question obj
	:return: list of string, option names
	"""
	option_obj_set = question_obj.get_options_set_order_by_index()
	choice_list = [option.choice_name for option in option_obj_set]

	return choice_list


class SurveyService:
	survey = None
	questions = None
	question_map = {
		'SINGLE': SingleChoiceQuestion,
		'MULTIPLE': MultipleChoiceQuestion
	}

	def __init__(self, survey_obj, question_obj_set):
		"""
		init the survey service from database objects
		:param survey_obj: The database survey obj
		:param question_obj_set: the database question object set
		"""
		self.survey_obj = survey_obj
		self.question_obj_set = question_obj_set

	def build_survey(self):
		survey_name = self.survey_obj.survey_name  # not important can be deleted
		survey_id = self.survey_obj.survey_id  # not important can be deleted
		if not self.questions:
			self.build_questions()
		self.survey = Survey(survey_name=survey_name, survey_id=survey_id, questions=self.questions)

	def build_questions(self):
		question_list = []
		for question_obj in self.question_obj_set:
			question = self.question_map[question_obj.question_type](question_name='',
			                                                         description='',
			                                                         weight=question_obj.weight,
			                                                         choices=get_clean_options_from_question(question_obj),
			                                                         max_num_choice=question_obj.max_choice)
			question_list.append(question)
		self.questions = question_list


class StudentService:
	def __init__(self, student_obj_set, answer_obj_set, survey_service_obj):
		pass
