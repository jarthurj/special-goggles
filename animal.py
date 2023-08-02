class Animal(object):
	def __init__(self, name, health = 50):
		self.name = name
		self.health = health

	def walk(self):
		self.health -= 1

	def run(self):
		self.health -= 5

	def display_health(self):
		print(self.health)
