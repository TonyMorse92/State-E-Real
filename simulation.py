import random as rand

class House:

	def __init__(self, price, num_bedrooms, num_stories):
		self.price = price
		self.num_bedrooms = num_bedrooms
		self.num_stories = num_stories

homes = []

for _ in range(0,10000):
	home = House(rand.uniform(100_000,150_000), rand.choice([1,2,4]), rand.choice([1,2]))

	#print(f"The price is: ${home.price}\nThere are {home.num_bedrooms} bedroom(s)\nAnd it is a {home.num_stories} story house.\n")
	homes.append(home)

highest_price = 0

for home in homes:
	if home.price > highest_price:
		highest_price = home.price

print(f"The highest price is: {highest_price}")
