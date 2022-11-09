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

	score = (num_unique_choice / team_size)

	return score
