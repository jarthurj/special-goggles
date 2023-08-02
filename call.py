from datetime import datetime


class Call(object):
	call_count = 0
	print("butt")
	def __init__(self,caller_name, phone_number, reason, time=datetime.now()):
		Call.call_count += 1
		self.call_id = Call.call_count
		self.caller_name = caller_name
		self.phone_number = phone_number
		self.time = time
		self.reason = reason
	def display_call(self):
		print("call_id:",self.call_id)
		print("caller_name:",self.caller_name)
		print("phone_number:",self.phone_number)
		print("time:",self.time)
		print("reason:",self.reason)
