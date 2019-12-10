def recursion(dataset):
    brends = list()
    for i in range(len(dataset[0])):
        if len(dataset[0][i]) > 10:
            brends.append(dataset[0][i])

    for j in range(len(brends)):
        brend = brends[j]
        size = dataset.values("brend", "")