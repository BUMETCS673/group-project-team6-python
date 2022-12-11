from survey.models import Option, Question, AnswerSheet, ChoiceSingle, ChoiceMultiple
from account.models import Student
from django.shortcuts import render, Http404
from django.contrib import messages
import csv


def reorder(question):
	existing_options = Option.objects.filter(question=question)
	if not existing_options.exists():
		return
	number_of_option = existing_options.count()
	new_ordering = range(0, number_of_option)

	for order, option in zip(new_ordering, existing_options):
		option.order = order
		option.save()


def save_question_set(IO_string, survey):
	"""read and save csv to a survey"""
	"""
	note: question type: 1 is mul,0 is single
	first row is the header
	return [# of success, total question input]
	"""

	reader = csv.DictReader(IO_string)
	total_question = reader.line_num
	count_question_save = 0
	for question_idx, question in enumerate(reader):
		try:
			question_index = int(question['question_index'])
			question_type = "SINGLE" if str(question['question_type']) == '0' else "MULTIPLE" if str(question[
				                                                                                         'question_type']) == '1' else None
			max_choice = int(question['max_choice'])
			weight = int(question['weight'])
			name = str(question['name'])
			description = str(question['description'])
			options = question['options'].splitlines()
			question_obj = save_question(question_index=question_index,
			                             question_type=question_type,
			                             max_choice=max_choice,
			                             weight=weight,
			                             question_name=name,
			                             description=description,
			                             survey=survey)
			for choice_index, option_name in enumerate(options):
				save_option(choice_index=choice_index, choice_name=option_name, question=question_obj)
			count_question_save += 1
		except Exception as e:
			print(f"error{question}+++++++++++", e)
		print([count_question_save, total_question])
	return [count_question_save, total_question]


def save_question(question_index, question_type, max_choice, weight, question_name, description, survey):
	"""save a question to the survey"""
	question, _ = Question.objects.get_or_create(survey=survey,
	                                             question_index=question_index,
	                                             question_type=question_type,
	                                             max_choice=max_choice,
	                                             weight=weight,
	                                             question_name=question_name,
	                                             description=description
	                                             )
	return question


def save_option(choice_index, choice_name, question):
	"""save an option of a question"""
	option, _ = Option.objects.get_or_create(choice_index=choice_index,
	                                         choice_name=choice_name,
	                                         question=question)
	return option


def save_all_student_answer_set(IO_string, survey):
	"""read and save student answer set of a survey"""
	"""
	note: question type: 1 is mul,0 is single
	first row is the header
	return [# of success, total question input]
	"""
	reader = csv.DictReader(IO_string)

	for student_index, student_answers in enumerate(reader):
		try:
			name = str(student_answers['student_name'])
			email = str(student_answers['student_email'])
			student = save_student(email=email, name=name)
			question_set = survey.get_questions_set_order_by_index()
			answer_sheet = save_answer_sheet(student, survey)
			answer_sheet = save_student_answers(answer_sheet=answer_sheet,
			                                    question_set=question_set,
			                                    answer_set=student_answers)
		except Exception as e:
			error = f"error happen student_index:{student_index},{str(e)} "
			raise Exception(error)
	return


def save_student(email, name):
	"""save student from the csv"""
	student, _ = Student.objects.get_or_create(name=name,
	                                           email=email)
	return student


def save_answer_sheet(student, survey):
	"""save answer sheet"""
	previous_answer_sheet = AnswerSheet.objects.filter(student=student,
	                                                   survey=survey).last()  # get the last create answer sheet or none
	if previous_answer_sheet:
		# if has previous answer, set previous answer sheet to inactive
		previous_answer_sheet.active = False
		previous_answer_sheet.save()
	# new answer sheet
	answer_sheet = AnswerSheet(student=student,
	                           survey=survey,
	                           active=True)  # default active is true
	answer_sheet.save()
	print(f"saved student answer sheet")
	return answer_sheet


def save_student_answers(answer_sheet, question_set, answer_set):
	"""
	save all of a student's answers to an answer sheet
	:param answer_sheet: object of AnswerSheet
	:param question_set: order collection of the question in survey by index
	:param answer_set: dict, {'question_x': str y}, x is the index of the question in survey, y is the option index
	:return: the answer sheet
	"""
	if len(question_set) != len(answer_set) - 2:
		raise Exception("student response is not valid")

	for question_index, question in enumerate(question_set):
		if question.question_type == "SINGLE":
			student_choice = int(
				answer_set[f'question_{question_index}'])  # should be the int of index of single choice
			choice_option = question.get_option_by_index(option_index=student_choice)
			ChoiceSingle(option=choice_option, answer_sheet=answer_sheet, question=question).save()

		elif question.question_type == "MULTIPLE":
			student_choices = [int(i) for i in str(answer_set[f'question_{question_index}']).split(
				',')]  # student choices would be a list, choice at least 1
			for rank, student_choice in enumerate(student_choices):
				# iterate over all choice and save
				choice_option = question.get_option_by_index(option_index=student_choice)
				ChoiceMultiple(rank=rank, option=choice_option, answer_sheet=answer_sheet, question=question).save()
		print(f"saved{question.question_name}")
	return answer_sheet
