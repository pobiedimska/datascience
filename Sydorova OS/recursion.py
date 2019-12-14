
count = 0
ind = 0
def count_zipcode(dataset,count,ind):
    if dataset['zipcode'][ind] == 1:
        count+=1
    ind+=1
    if ind<len(dataset['zipcode']):
        count_zipcode(dataset,count,ind)
    else:
        return 1



count_zipcode(dataset,count,ind)
print("Кількість дерев з zipcode = 1:",count)