from survey.models import Survey, AnswerSheet
from .models import ResultTeam, StudentTeam, ResultQuestionScore
from account.models import Student
from .services.services import SurveyService, StudentAnswerService, iGroupService


def run_algorithm(config_instance_obj, instance_obj):
	"""
	run the algorithm
	return: All teams
	"""
	# run the algorithm
	max_num_pass = config_instance_obj.max_num_pass
	num_group = config_instance_obj.num_group
	# run services
	# survey services
	survey_obj = Survey.objects.get(instance=instance_obj)
	question_obj_set = survey_obj.get_questions_set()
	survey_service = SurveyService(survey_obj, question_obj_set)
	survey_service.build_survey()
	# student answer service
	answer_sheet_obj_set = AnswerSheet.objects.filter(survey=survey_obj, active=True)

	student_obj_set = [answer_sheet_obj.student for
	                   answer_sheet_obj in answer_sheet_obj_set]  # should be unique student

	student_answer_service = StudentAnswerService(student_obj_set=student_obj_set,
	                                              answer_sheet_obj_set=answer_sheet_obj_set,
	                                              survey=survey_service.survey,
	                                              survey_obj=survey_obj)
	student_answer_service.build_students()
	student_answer_service.build_answer_sheets()
	student_answer_service.response_survey()
	# iGroup service
	iGroup_service = iGroupService(students_target=student_answer_service.students,
	                               num_team=num_group,
	                               survey_target=survey_service.survey,
	                               num_pass=max_num_pass)
	result = iGroup_service.run()

	return result


def save_result(config_instance_obj, result):
	"""save result to this configuration"""

	save_result_teams(config_instance_obj=config_instance_obj,
	                  result=result)


def save_result_teams(config_instance_obj, result):
	"""create the result teams from the algorithm result"""
	for team_index, team in enumerate(result):
		team_size = team.get_team_size()
		team_name = team.team_name
		total_team_score = team.get_total_score()
		student_list = team.team_members
		result_team_obj = ResultTeam(config_instance=config_instance_obj,
		                             team_size=team_size,
		                             team_index=team_index,
		                             team_name=team_name,
		                             total_score=total_team_score)
		result_team_obj.save()
		# save result student to the result team
		for student in student_list:
			student_email = student.email
			# save student to the result team
			save_result_student(result_team_obj=result_team_obj,
			                    student_email=student_email)
		single_choice_question_scores = team.get_single_choice_scores()
		multiple_choice_question_scores = team.get_mul_choices_scores()
		total_scores = single_choice_question_scores | multiple_choice_question_scores
		survey_obj = config_instance_obj.get_survey()

		# save result question scores to the result team
		for question_index, score in total_scores.items():
			save_question_score(survey_obj=survey_obj,
			                    question_index=question_index,
			                    score=score,
			                    result_team_obj=result_team_obj)

	return


def save_result_student(result_team_obj, student_email):
	"""save student to the result team"""
	student_obj = Student.objects.get(email=student_email)
	student_team = StudentTeam(student=student_obj,
	                           result_team=result_team_obj)
	student_team.save()
	return student_team


def save_question_score(survey_obj, question_index, score, result_team_obj):
	"""save question scores in a team"""
	question_obj = survey_obj.get_question_by_index(question_index=question_index)
	question_type = question_obj.question_type
	question_weight = question_obj.weight
	result_question_score = ResultQuestionScore(result_team=result_team_obj,
	                                            question=question_obj,
	                                            question_score=score,
	                                            question_type=question_type,
	                                            question_weight=question_weight)
	result_question_score.save()
	return result_question_score
