from hudymvm.dataset_structure import dataset

def recursion(value1):
    if not value1:
        return 0
    return 1 + recursion(value1[:-1])

for values in dataset.values():
    value = values['name'].split()
if len(value) > 3:
    for values in dataset.values():
        value1 = values['categories'].split(',')
        print('Number of categories:', recursion(value1), value1)