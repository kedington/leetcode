class Question:

	def __init__(self, name, number, difficulty):
		self.name = name.capitalize()
		self.number = number
		self.link = "https://leetcode.com/problems/{}/".format(name)
		self.difficulty = difficulty
		self.file_name = "{0}_{1}".format(number, name)

