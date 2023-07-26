import numpy as np

class farmer:

	 def __init__(self, resilience=100):
	 	'''
	 		This method initializes the farmer class.
	 		It initializes the crop and flexibility attributes
	 	'''
	 	crops = ['cotton', 'figs', 'almonds', 'tomatoes', 'grapes']
	 	self.crop = crops[np.random.randint(0, 5, 1)[0]]
	 	self.flex = np.random.randint(1, 101, 1)[0] #the lower the less flexible
	 	self.res = resilience
	 def update(self, max_price, max_crop, curr_price):
	 	'''
	 		This method updates the farmer class annually
	 		Args:
	 			max_price: maximum crop price that year
	 			max_crop: maximum crop that year
	 			curr_price: price of the farmer's current crop
	 	'''
	 	# print("flex = " + str(self.flex))
	 	flex = self.res / self.flex
	 	diff = abs(max_price / curr_price)
	 	ultimate_randomizer = np.random.randint(0, 3)
	 	if ((flex < diff) or curr_price < 0) and ultimate_randomizer == 0:
	 		self.crop = max_crop
	 		self.flex = int(np.min((self.flex, 10)))
	 		# print("1 = " + str(self.flex))					
	 	else:
	 		if self.crop == max_crop:
	 			self.flex = int(np.max((self.flex - 2, 1)))
	 			# print("2 = " + str(self.flex))
	 		else:
	 			self.flex = int(np.min((self.flex + diff, 100)))
	 			# print("3 = " + str(self.flex))