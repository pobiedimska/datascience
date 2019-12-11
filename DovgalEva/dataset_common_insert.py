from DovgalEva.dataset_structure import dataset
from DovgalEva.validator import lib
import re


def insert_common_data(dataset):
    if not isinstance(dataset, list):
        print(f'Your dataset is not valid!')
        return -1

    # считается, что файл существует и находится там же, где и этот
    descr = open('descriptions.txt', 'r')
    descr = descr.read().split(sep='\n')
    pattern = re.compile('(\w+)\s-\s(\w+);\s(.+)')
    data = {}
    for i in range(len(descr)):
        option = re.match(pattern, descr[i])
        key = option.group(1)
        print(f'\n{key} is {option.group(2)}. Description:\n{option.group(3)}')
        data[key] = eval(f"lib.{key}_validator(input(f'{key} = '))")
    dataset.append(data)

    return dataset


insert_common_data(dataset)
for i in range(len(dataset)): print(dataset[i])
