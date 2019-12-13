dict_keys = list(dataset.keys())


def price_and_rooms(dataset, keys):
    if not len(keys):
        return False
    else:
        if dataset[keys[0]]['beds'] > 2 or dataset[keys[0]]['price'] > 100:
            for k in dataset[keys[0]].keys():
                if k != 'beds':
                    print(dataset[keys[0]][k])
            print('\n')
        return price_and_rooms(dataset, keys[1:])

price_and_rooms(dataset, dict_keys)