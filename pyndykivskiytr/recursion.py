def info(dataset):
	print("Table info that satisfies conditions : ")
	print("\nProvider id\t\tCity\t\tTotal lupa episodes")
	for provider_id in dataset.keys():
		if(dataset[provider_id]["average_age"]>30) and (dataset[provider_id]["total_lupa_episodes"]>2):
			print(provider_id + '\t\t   ' + dataset[provider_id]["city"] + ' '*(30-len(dataset[provider_id]["city"])) + str(dataset[provider_id]["total_lupa_episodes"]))

