from DovgalEva.dataset_structure import dataset


def insert_data(data, dataset):
    if not isinstance(data, dict) or len(data.keys()) != 4\
            or data.keys() != dataset[0].keys():
        print(f'Your data or keys is/are not valid!')
        return -1
    if not isinstance(dataset, list):
        print(f'Your dataset is not valid!')
        return -1

    dataset.append(data)


# >>> test
# my_friend = {
#     'provider_id': 58419,
#     'city': 'BROOKLYN',
#     'zip_code': 11222,
#     'total_episodes_non_lupa': 2570
# }
# insert_data(my_friend, dataset)

# >>> check:
# for i in range(len(dataset)):
#     print(dataset[i].items())

