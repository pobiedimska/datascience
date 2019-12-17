from Sazonenko.dataset_structure import dataset

keys = list(dataset.values())

def recursion (keys, counter = 0):
    if len(keys) == 0 :
        return 0

    if list(next(iter(list(dataset.values()))).values())[0] == 'good':
        counter += 1
    print(counter)
    return recursion(keys[1:], counter)

# print(recursion(keys))


if __name__ == '__main__':
    recursion(keys)