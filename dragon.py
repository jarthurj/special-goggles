from animal import Animal

class Dragon(Animal):
	def __init__(self, name, health=170):
		super(Dragon, self).__init__(name)
		self.health = health
	def fly(self):
		self.health -= 10

	def display_health(self):
		super(Dragon, self).display_health()
		print("I am dragon")