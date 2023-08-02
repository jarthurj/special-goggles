class CallCenter(object):
	def __init__(self):
		self.calls = []
		self.queue_size = len(self.calls)

	def add_call(self, call):
		self.calls.append(call)
		self.queue_size = len(self.calls)
	def remove(self):
		del self.calls[0]
		self.queue_size = len(self.calls)

	def info(self):
		print("Total number of calls: ", self.queue_size)
		for call in self.calls:
			call.display_call()
			print("\n")


