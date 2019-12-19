from dovgaleo.dataset_structure import dataset


def recursion(dataset):
    if len(dataset) == 0:
        return 0

    condition = 0
    provider_ids = list(dataset.keys())

    for key, value in dataset[provider_ids[0]].items():
        if key == 'city' and value == 'IRWINDALE':
            condition += 1
        elif key == 'total_episodes_non_lupa' and value > 1000:
            condition += 1
    if condition == 2:
        print(provider_ids[0])
        print(dataset[provider_ids[0]].get('zip_code'))
        print(dataset[provider_ids[0]].get('city'))

    del dataset[provider_ids[0]]
    recursion(dataset)


recursion(dataset.copy())
