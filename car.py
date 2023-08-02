class Car:
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = 12
		if price > 10000:
			self.tax = 15
	def display_all(self):
		print(f"price:{self.price}")
		print(f"speed:{self.speed}")
		print(f"fuel:{self.fuel}")
		print(f"mileage:{self.mileage}")
		print(f"tax:{self.tax}")