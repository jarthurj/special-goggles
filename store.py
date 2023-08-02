from product import Product

class Store:
	def __init__(self, owner, location):
		self.owner = owner
		self.location = location
		self.products = []

	def add_product(self, product):
		self.products.append(product)

	def remove_product(self, product):
		self.products.remove(product)

	def inventory(self):
		for product in self.products:
			product.display_info()

if __name__ == '__main__':
	store1 = Store("someguy", "corner")
	store1.prodcuts.append(Product(2,"lucky charms",1,"GM"))
	store1.prodcuts.append(Product(2,"total",1,"GM"))
	store1.inventory()