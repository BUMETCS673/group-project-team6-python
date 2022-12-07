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
    # guard
    if team_size == 0 or max_num_choice == 0 or team_size is None or max_num_choice is None or option_scores is None:
        print("invalid input")
        return -9999

    # drop the scores with occurrence less or equal to 1
    option_scores = [s for s in option_scores if s[1] > 1]

    # recalculate the max_num_choice
    num_valid_option = len(option_scores)

    # if no valid option, score set to 1
    if num_valid_option == 0:
        return 1

    # calculate the total scores

    # 1. need to find the base
    def expression(x): return x ** 2
    base = (team_size ** 2) * sum(expression(max_num_choice - i) for i in range(num_valid_option))
    sum_b = sum(expression(i[0]) for i in option_scores)

    score = 1 - (sum_b / base)

    return round(score, 3)
