from dovgaleo.dataset_structure import dataset


def recursion(dataset, provider_ids=[]):
    if provider_ids == 0:
        return recursion(dataset, provider_ids=list(dataset.keys()))

    condition = 0
    for key, value in dataset[provider_ids[0]].items():
        if key == 'city' and value == 'IRWINDALE':
            condition += 1
        elif key == 'total_episodes_non_lupa' and value > 1000:
            condition += 1
    if condition == 2:
        print(provider_ids[0])
        print(dataset[provider_ids[0]].get('zip_code'))
        print(dataset[provider_ids[0]].get('city'))

    if len(provider_ids[1:]) == 0: return
    recursion(dataset, provider_ids=provider_ids[1:])


recursion(dataset.copy())
