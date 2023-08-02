class MathDojo(object):
	def __init__(self, value):
		self.value = value

	def add(self, *args):
		summer = 0
		for arg in args:
			if hasattr(arg, '__iter__'):
				for num in arg:
					summer += num
			else:
				summer += arg
		self.value += summer
		return self

	def subtract(self, *args):
		subber = 0
		for arg in args:
			if hasattr(arg, '__iter__'):
				for num in arg:
					subber += num
			else:
				subber += arg
		self.value -= subber
		return self
	def result(self):
		print(self.value)