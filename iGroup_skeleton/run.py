class Run:
	def __init__(self):
		self.survey = None
		self.max_passes = 20
		self.team = {}


	@property
	def max_passes(self):
		return self.max_passes

	@max_passes.setter
	def max_passes(self,num_passes):
		self.max_passes = num_passes

	def run_allocation(self):
		#run the algorithm base on the config
		#return the last instance team formation
		pass