from animal import Animal

class Dog(Animal):
	def __init__(self, name, health=150):
		super(Dog, self).__init__(name)
		self.health = health
	def pet(self):
		self.health += 5

