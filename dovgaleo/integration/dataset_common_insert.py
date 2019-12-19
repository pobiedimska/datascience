from dovgaleo.integration.dataset_structure_common import dataset
from dovgaleo.integration import validator


def insert_common_data(dataset):
    if not isinstance(dataset, dict):
        print('Your dataset is not valid')
        return -1

    keys = ['provider_id', 'city', 'zip_code', 'total_episodes_non_lupa',
            'percent_of_beneficiaries_with_ra_oa', 'percent_of_beneficiaries_with_stroke']

    provider_id = 0
    for i in range(6):
        while True:
            value, check = input(f'{keys[i]} = '), 0

            if keys[i] == keys[0]: check = validator.provider_id_validator(value)
            if keys[i] == keys[1]: check = validator.city_validator(value)
            if keys[i] == keys[2]: check = validator.zip_code_validator(value)
            if keys[i] == keys[3]: check = validator.total_episodes_non_lupa_validator(value)
            if keys[i] == keys[4]: check = validator.percent_of_beneficiaries_with_ra_oa_validator(value)
            if keys[i] == keys[5]: check = validator.percent_of_beneficiaries_with_stroke_validator(value)

            if check is True: break

        if i == 0:
            provider_id = value
            dataset[provider_id] = {}
        else:
            dataset[provider_id][keys[i]] = value


insert_common_data(dataset)

print('\ndataset:')
for key, value in dataset.items():
    print('id', key, value)
