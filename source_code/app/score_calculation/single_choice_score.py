"""
single choice question score calculation

"""


def cal_single_score(team_size, num_unique_choice):
	"""
	given team-size, number of unique choice
	@param team_size:the size of the team
	@param num_unique_choice: the number of unique choice for this question
	@return: the single choice choose score
	"""
	# then calculate the score for this single choice problem

	# Judge 0, None team_size. Judge num_unique_choice
	if team_size == 0 or team_size is None or num_unique_choice is None:
		print("invalid input")
	else:
		return num_unique_choice / team_size

