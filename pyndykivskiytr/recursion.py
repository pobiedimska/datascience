"""
def info(dataset):
	print("Table info that satisfies conditions : ")
	print("\nProvider id\t\tCity\t\tTotal lupa episodes")
	for provider_id in dataset.keys():
		if(dataset[provider_id]["average_age"]>30) and (dataset[provider_id]["total_lupa_episodes"]>2):
			print(provider_id + '\t\t   ' + dataset[provider_id]["city"] + ' '*(30-len(dataset[provider_id]["city"])) + str(dataset[provider_id]["total_lupa_episodes"]))
"""
from dataset_structure import dataset

def info(dataset, iterator=0):

	keys=list(dataset.keys())

	if(iterator>len(keys)-1):
		return  

	else:	

		if(dataset[keys[iterator]]["average_age"]>30) and (dataset[keys[iterator]]["total_lupa_episodes"]>2):
			print(keys[iterator] + '\t\t   ' + dataset[keys[iterator]]["city"] + ' '*(30-len(dataset[keys[iterator]]["city"])) + str(dataset[keys[iterator]]["total_lupa_episodes"]))

		info(dataset, iterator+1)

print("Table info that satisfies conditions : ")
print("\nProvider id\t\tCity\t\tTotal lupa episodes")
info(dataset)
