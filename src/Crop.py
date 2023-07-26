import numpy as np

class crop:

	def __init__(self, water = 0):
		'''
			Initializes the crop class. The crop classes contains the prices and water usage
			of all five crops in order: {cotton, figs, almonds, tomatoes, grapes}
		'''
		self.crop_prices = {
			"cotton": 744,
			"figs": 712,
			"almonds": 3210,
			"tomatoes": 360,
			"grapes": 712
		}
		self.crop_water = {
			"cotton": 4029,
			"figs": 3350,
			"almonds": 16095,
			"tomatoes": 214,
			"grapes": 608
		}
		self.water = water
	def update(self, farmers, change_water = 0):
		'''
			This updates the crop class based on shifting prices.
			Args:
				farmers: A dictionary of 5 crops and numbers representing the total number of farmers
				for each crop
				water: The price of water per gallon
			Returns:
				prices: a dictionary of the prices of each crop that year
		'''
		if (change_water != 0):
			self.water = change_water
		values = farmers.values()
		total = sum(values)
		prices = {}
		for key in self.crop_prices:
			diff = np.max((farmers[key], 1)) / (total)
			new_price = int((self.crop_prices[key] - self.water * self.crop_water[key]) / (5 * diff))
			prices[key] = new_price
		return prices



