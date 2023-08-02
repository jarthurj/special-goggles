class Product:
	def __init__(self, price, name, weight, brand):
		self.price = price
		self.name = name
		self.weight = weight
		self.brand = brand
		self.status = "for sale"

	def sell(self):
		self.status = "sold"
		return self

	def add_tax(self):
		return self.price+(self.price*.1)


	def return_item(self, return_reason, item_status):
		self.return_reason = return_reason
		if item_status == 'defective':
			self.status = 'defective'
			self.price = 0
		elif item_status == 'new':
			self.status = 'for sale'
		elif item_status == 'used':
			self.status = 'used'
			self.price = self.price*.8
		return self
	def display_info(self):
		print(f"price:{self.price}")
		print(f"name:{self.name}")
		print(f"weight:{self.weight}")
		print(f"brand:{self.brand}")
		print(f"status:{self.status}")

if __name__ == '__main__':
	p1 = Product(2,"lucky charms",1,"GM")
	p2 = Product(2,"total",1,"GM")
	p1.display_info()
	p2.display_info()