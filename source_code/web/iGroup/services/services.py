"""this includes all the services"""
from .app.survey import Survey
from .app.question import SingleChoiceQuestion, MultipleChoiceQuestion
from .app.user import Student
from .app.instance import Instance


class iGroupService:
	result = None

	def __init__(self, students_target, num_team, survey_target, num_pass):
		self.students_target = students_target
		self.num_team = num_team
		self.survey_target = survey_target
		self.num_pass = num_pass
		self.instance = Instance(num_pass=num_pass, students_target=students_target, num_team=num_team,
		                         survey_target=survey_target)

	def run(self):
		self.result = self.instance.run_instance()
		for team in self.result:
			print(f"_______{team.team_name}______")
			for team_member in team.team_members:
				print(team_member.name)
			print('______________________________')

		return self.result


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
			                                                         choices=get_clean_options_from_question(
				                                                         question_obj),
			                                                         max_num_choice=question_obj.max_choice)
			question_list.append(question)
		self.questions = question_list


class StudentAnswerService:
	students = []
	answer_sheets = {}

	def __init__(self, student_obj_set, answer_sheet_obj_set, survey_obj, survey):
		self.student_obj_set = student_obj_set
		self.answer_sheet_obj_set = answer_sheet_obj_set
		self.survey_obj = survey_obj
		self.survey = survey

	def build_students(self):
		"""build student instance"""
		if self.students:
			return
		id = 0
		for student_obj in self.student_obj_set:
			name = student_obj.name
			email = student_obj.email
			student = Student(email=email, name=name, user_id=id)
			self.students.append(student)
			id += 1

	def build_answer_sheets(self):
		if not self.students:
			self.build_students()

		for student_index, student_obj in enumerate(self.student_obj_set):
			answer_sheet_obj = self.answer_sheet_obj_set.get(student=student_obj)
			answer_single_choice_set = answer_sheet_obj.answer_single_choice.all()
			answer_multiple_choice_set = answer_sheet_obj.answer_multiple_choice.all()
			response_dic = dict()
			for answer in answer_single_choice_set:
				response_dic[answer.option.question.question_index] = answer.option.choice_index
			for answer in answer_multiple_choice_set:
				if answer.option.question.question_index in response_dic:
					response_dic[answer.option.question.question_index] = response_dic[
						                                                      answer.option.question.question_index] | {
						                                                      answer.rank: answer.option.choice_index}
				else:
					response_dic[answer.option.question.question_index] = {answer.rank: answer.option.choice_index}
			self.answer_sheets[student_index] = response_dic

	def response_survey(self):
		"""response to the survey"""
		if not self.students:
			# build student first if not built yet
			self.build_students()

		if not self.answer_sheets:
			self.build_answer_sheets()

		for student_index, student in enumerate(self.students):
			student.answer_survey(self.survey, self.answer_sheets[student_index])
