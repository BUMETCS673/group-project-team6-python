
class Instance:
	def __init__(self,current_pass,team_formation):
		self.current_pass = current_pass
		self.team_formation = team_formation
		self.students = []  # all students for this instance
		self.teams = {}   # rank, team pair
		self.init_team_method = "random"

	def init_team(self):
		pass

	def sort_team(self):
		pass

	def swap_student(self):
		pass

	def run_instance(self):
		#run the swap for all students
		pass

