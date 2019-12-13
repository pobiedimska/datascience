def recursion(dataset, i=0):

    host_id = list(dataset.keys())[i]
    country = list(dataset[host_id].keys())[0]

    if list(dataset[host_id][country].keys())[0] > 1 and list(dataset[host_id][country].values())[0] > 10:
        print(list(dataset[host_id][country].keys())[0])
        print(list(dataset[host_id][country].values())[0])

    if i == len(list(dataset.keys()))-1:
        return

    recursion(dataset, i+1)




dataset = {956883:{'United Sates':{1:207}},
           239585:{'United States':{1:181}},
           2315558:{'United States':{2:41}}}

def recursion(dataset, i=0):
    for i in range(len(dataset.keys())):
        host_id = (list(dataset.keys())[i])
        for j in range(len(dataset[host_id])):
            country = (list(dataset[host_id].keys())[j])
            print(list(dataset[host_id][country].keys())[0])
            print(list(dataset[host_id][country].values())[0])
