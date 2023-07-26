from Crop import crop
from Farmer import farmer

def crop_sanity_test():
	crop = crop()
	farmers = {
		"cotton": 1,
		"figs": 1,
		"almonds": 1,
		"tomatoes": 1,
		"grapes": 6
	}
	print(crop.crop_prices)
	print(crop.crop_water)
	print(crop.update(farmers))


def farmer_sanity_test():
	num_farmers = 5
	farmers = []
	for i in range(num_farmers):
		farmers.append(farmer())
	for i in range(len(farmers)):
		print(farmers[i].crop)
		print(farmers[i].flex)
	for i in range(len(farmers)):
		farmers[i].update(50, 'almonds', 25)
		print(farmers[i].crop)
		print(farmers[i].flex)
farmer_sanity_test()