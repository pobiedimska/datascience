from dovgaleo.integration.dataset_structure_common import dataset
from dovgaleo.integration import validator
import re


def insert_common_data(dataset):
    if not isinstance(dataset, dict):
        print(f'Your dataset is not valid!')
        return -1

    # считается, что файл существует, заполнен верно и находится там же, где и этот :)))
    with open('descriptions.txt', 'r') as f:
        descr = f.read().split(sep='\n')
    pattern = re.compile('(\w+)\s-\s(\w+);\s(.+)')
    print(descr)
    data, provider_id = {}, 0
    for i in range(len(descr)):
        option = re.match(pattern, descr[i])
        key = option.group(1)
        print(f'\n{key} is {option.group(2)}. Description:\n{option.group(3)}')
        while True:
            value = eval(f"validator.{key}_validator(input(f'{key} = '))")
            if value is not None: break
        if i == 0:
            data[value] = {}
            provider_id = list(data.keys())[0]
        data[provider_id][key] = value
    dataset.update(data)
    return dataset


insert_common_data(dataset)

print('\ndataset:')
for key, value in dataset.items():
    print('id', key, value)
