def recursion(dataset, i=0):

    host_id = list(dataset.keys())[i]
    country = list(dataset[host_id].keys())[0]

    if list(dataset[host_id][country].keys())[0] > 1 and list(dataset[host_id][country].values())[0] > 10:
        print(list(dataset[host_id][country].keys())[0])
        print(list(dataset[host_id][country].values())[0])

    if i == len(list(dataset.keys()))-1:
        return

    recursion(dataset, i+1)