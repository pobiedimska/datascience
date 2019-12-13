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

#
# dict_values = list(dataset.values())
#
# def recursion(dataset, dict_values, count = 0, n = 0):
#     if n>=len(dataset):
#         return count
#     else:
#         if len(list(dataset.get['name']))


# def recursion(dataset,index, n=0):
#
#     for values in list(dataset.values()):
#         if len(values['name'].split()) > 3:
#
#             for values in list(dataset.values()):
#                 value = values['categories'].split(',')
#                 print(value[n])
#
#
#                 if len(value) == index:
#                     return 0
#
#                 return 1 + recursion(dataset, index + 1, n+1)
#
#
# print(recursion(dataset,0))
#

# def list_of_names():
#     list_of_names = []
#     for values in dataset.values():
#         list_of_names.append(values['name'])
#     return list_of_names
#
# def list_of_categories():
#     list_of_categories = []
#     for values in dataset.values():
#         list_of_categories.append(values['categories'])
#     return list_of_categories
#
# print(list_of_names())
# print(list_of_categories())
#
# def recursion(dataset, n=0, count=0):
#
#     keys = list(dataset.keys())
#     values = list(dataset.values())
#
#     if n>=len(values):
#         return count
#     else:
#         if len(dataset[keys[n]].get('name').split()) > 3:
#             for value in dataset[keys[n]].get('categories').split(','):
#                 print(value)
#                 if value:
#                     count += 1
#             return recursion(dataset, n + 1, count)
#
#
#
#
# print(recursion(dataset))

# v = list(dataset.values())
# print(len(v))
#     for values in dataset.values():
#         value = values['name'].split()
#
#         if len(value) > 3:
#             for values in list(dataset.values()):
#                 value1 = values['categories'][n]
#
#                 if not value1:
#                     return 0
#                 return 1 + recursion(dataset, n+1)
#
# print('Number of categories:', recursion(dataset))

# s = list(dataset.keys())
# print(len(dataset[s[0]].get('name').split()))