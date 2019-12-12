from dovgaleo.dataset_structure import dataset
from dovgaleo.validator import lib
import re


def insert_common_data(dataset):
    if not isinstance(dataset, dict):
        print(f'Your dataset is not valid!')
        return -1

    # считается, что файл существует и находится там же, где и этот
    descr = open('descriptions.txt', 'r')
    descr = descr.read().split(sep='\n')
    pattern = re.compile('(\w+)\s-\s(\w+);\s(.+)')
    provider_id = 0
    data = {}
    for i in range(len(descr)):
        option = re.match(pattern, descr[i])
        key = option.group(1)
        print(f'\n{key} is {option.group(2)}. Description:\n{option.group(3)}')
        if i == 0:
            key = eval(f"lib.{key}_validator(input(f'{key} = '))")
            data[key] = {}
            provider_id = list(data.keys())[0]
        else:
            data[provider_id][key] = eval(f"lib.{key}_validator(input(f'{key} = '))")
    dataset.update(data)

    return dataset


insert_common_data(dataset)

print('\ndataset:')   # is insert correct?:
for key, value in dataset.items():
    print('id', key, value)
