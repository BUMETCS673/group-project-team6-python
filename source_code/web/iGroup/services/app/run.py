"""
class for instructor specific parameter
"""
from instance import Instance

class Run:

	def __init__(self, num_max_pass, num_team, survey_target, student_pool):
		"""

		@param num_max_pass: the max number of pass allowed for climbing hill algorithm
		@param num_team: the number of team formation
		@param survey_target: the target survey for this allocation
		"""
		self.num_max_pass = num_max_pass
		self.num_team = num_team
		self.survey = survey_target
		self.students = student_pool

	def run(self):
		"""
		run the allocation algorithm
		@return: the team formation
		"""


		pass 