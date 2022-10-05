class Team:
	total_score = 0

	def __init__(self, team_size, team_name, members, **kwargs):
		# self.team_id = uuid
		self.team_size = team_size
		self.team_name = team_name
		self.team_members = members  # list of student

	@property
	def team_members(self):
		print(f"show group{self.team_name} members:{self.members}")
		return self.team_members

	@team_members.setter
	def team_members(self,members):
		print("set team members")
		self.team_members = members

	@team_members.deleter
	def team_members(self):
		print("deleting all members in the team")
		del self.team_members

	def add_team_member(self,student):
		self.team_members.append(student)

	def get_single_choice_score(self):
		pass

	def get_mul_choices_score(self):
		pass

	def get_sch_score(self):
		pass

