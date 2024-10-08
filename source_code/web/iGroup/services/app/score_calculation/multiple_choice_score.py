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
	option_scores = [s for s in option_scores if s[1] > 1]

	# recalculate the max_num_choice
	num_valid_option = len(option_scores)

	# if no valid option, score set to 1
	if num_valid_option == 0:
		score = 1
		return score
	# calculate the total scores

	# 1. need to find the base
	expression = lambda x: x ** 2
	base = (team_size ** 2) * sum(expression(max_num_choice - i) for i in range(num_valid_option))
	sum_b = sum(expression(i[0]) for i in option_scores)

	score = 1 - (sum_b / base)

	return round(score, 3)
