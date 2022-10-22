"""
The instance class, which is the team formation for each pass.
Swap happens here
"""
import random
from team import Team


class Instance:
	def __init__(self, num_pass, students_target, num_team, survey_target):
		"""
        @param num_pass: int, the maximum number of pass
        @param students_target: [student obj], the student pool
        @param num_team: [str], the list of team names
        @param survey_target: Survey, the survey the response corresponding to
        """
		self.num_pass = num_pass
		self.students_target = students_target
		self.num_team = num_team
		self.survey_target = survey_target

	def random_assignment(self):
		"""
        randomly assign the student to the given team
        @return: {team index, team]}
        """
		# shuffle student pool
		shuffled = random.sample(self.students_target,
		                         len(self.students_target))  # random.shuffle(self.students_target)

		# init team
		team_formation = []  # team

		for i in range(self.num_team):
			# init the team
			team = Team(team_name=f'team {i}', survey_target=self.survey_target)
			# assign the random select students to the team
			team.team_members = shuffled[i::self.num_team]
			team_formation.append(team)

		return team_formation

	def run_instance(self):
		"""
        Run the algorithm
        @return: the optimal team formation
        """
		# init randomized team formation [Team]
		teams = self.random_assignment()

		# print some info
		print(f"Initialization, the team scores:{[(team.team_name, team.get_total_score()) for team in teams]}")

		unswap, swap = 0, 0
		for iteration in range(self.num_pass):
			# start from the first team
			for index_team_1 in range(self.num_team):
				team_1 = teams[index_team_1]
				team_1_size = team_1.get_team_size()  # team 1 size is fixed
				for index_team_2 in range(index_team_1 + 1, self.num_team):
					team_2 = teams[index_team_2]
					team_2_size = team_2.get_team_size()
					ptr_team_1 = 0  # init team member pointer
					while ptr_team_1 < team_1_size:
						ptr_team_2 = 0
						while ptr_team_2 < team_2_size:
							# calculate the min score
							old_team_1_score = team_1.get_total_score()
							old_team_2_score = team_2.get_total_score()
							min_old_score = min(old_team_1_score, old_team_2_score)
							# perform swap
							student_team_1 = team_1.get_member_by_index(ptr_team_1)
							student_team_2 = team_2.get_member_by_index(ptr_team_2)
							team_1.replace_team_member(ptr_team_1, student_team_2)
							team_2.replace_team_member(ptr_team_2, student_team_1)
							swap += 1

							# get new min score
							new_team_1_score = team_1.get_total_score()
							new_team_2_score = team_2.get_total_score()
							min_new_score = min(new_team_1_score, new_team_2_score)

							if min_new_score <= min_old_score:
								unswap += 1
								# if swap lead to decrease scores, un-swap
								team_1.replace_team_member(ptr_team_1, student_team_1)
								team_2.replace_team_member(ptr_team_2, student_team_2)
							else:
								pass
							# update team 2 student
							ptr_team_2 += 1
						# update team 1 student
						ptr_team_1 += 1

		print(f"After swaps, the team scores:{[(team.team_name, team.get_total_score()) for team in teams]}")
		print(f"time of unswap {unswap}, time of swap {swap}")
		return teams


print()
