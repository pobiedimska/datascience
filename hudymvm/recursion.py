from hudymvm.dataset_structure import dataset

keys = list(dataset.keys())
length = len(keys)

def recursion(data, namecount, categoriescount, num):

    if num >= length:
        return 'success'

    id = keys[num]

    if data[id]['categories'] == '' and namecount > 3:
        print(categoriescount)
        return recursion(data, 0, 0, num + 1)

    if data[id]['name'] == '':
        categorieslist = data[id]['categories'].split(',')
        data[id]['categories'] = ','.join(categorieslist[1:])
        return recursion(data, namecount, categoriescount + 1, num)

    namelist = data[id]['name'].split()
    data[id]['name'] = ' '.join(namelist[1:])
    return recursion(data, namecount + 1, categoriescount, num)

print(recursion(dataset, 0, 0, 0))

