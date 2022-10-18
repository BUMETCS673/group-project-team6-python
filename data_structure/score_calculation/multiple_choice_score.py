"""
multiple choice question scores calculation
"""


def cal_multiple_score(team_size, max_num_choice, option_scores):
	"""
	calculate score for this team, given the team size, max number of choices
	@param team_size: the size of team
	@param max_num_choice: max number of unique of choice for the team members
	@param option_scores: option scores and its occurrence
	@return: the raw score
	"""
	# drop the scores with occurrence less or equal to 1
	option_scores = [score for score in option_scores if score[1] > 1]
	# calculate the total scores

	# 1. need to find the base
	expression = lambda x: x ** 2
	base = (team_size ** 2) * sum(expression(max_num_choice - i) for i in range(max_num_choice))
	sum_b = sum(expression(i[0]) for i in option_scores)
	score = 1 - sum_b / base

	return score
