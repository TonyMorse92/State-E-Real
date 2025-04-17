import random as rand

class House:

	def __init__(self, price, num_bedrooms, num_stories):
		self.price = price
		self.num_bedrooms = num_bedrooms
		self.num_stories = num_stories


for _ in range(0,10):
	t = House(rand.uniform(100_000,150_000), rand.choice([1,2,4]), rand.choice([1,2]))

	print(f"The price is: ${t.price}\nThere are {t.num_bedrooms} bedroom(s)\nAnd it is a {t.num_stories} story house.\n")
