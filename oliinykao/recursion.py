def recursion(dataset, sum = 0, brand_list = [], n = 0):
    if n == len(dataset):
        return sum
    if dataset[n].get("color") == "red" & dataset[n].get("brand") not in brand_list:
        sum += 1
        brand_list.add(dataset[n].get("brand"))
    n += 1
    recursion(dataset, sum, brand_list, n)