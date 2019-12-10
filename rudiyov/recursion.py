from rudiyov.dataset_structure import dataset


def get_value(database, search_key, last_key_in_dict, searched_array):
    """
    get some value
    :param database: dict , dataset
    :param search_key: name of wanted key
    :param last_key_in_dict: last key of your dictionary
    :param searched_array: empty array
    :return:list, array with all found value
    """
    for key in database.keys():
        if key == search_key:
            searched_array.append(database[key])
        elif isinstance(database[key], dict):
            get_value(database[key], search_key, last_key_in_dict, searched_array)
    if list(database.keys())[-1] == last_key_in_dict:
        return searched_array


def get_last_key(dictionary):
    """
    get last key
    :param dictionary: dict,dataset
    :return:with type of key, name of last key
    """
    return list(dictionary.keys())[-1]


__quantities = list()
__quantities = get_value(dataset, "sourceURLs", get_last_key(dataset), __quantities)
__prices = list()
__prices = get_value(dataset, "prices.count", get_last_key(dataset), __prices)


def search_price(data, quantities=__quantities,prices=__prices):
    """
     search max price with some criteria
    :param data: dict ,dataset
    :param quantities: list, value of sourceURLs
    :param prices: list, value of prices.count
    :return: float , max of prices witch meet the criteria
    """
    price_array = list()
    diction = dict(zip(quantities, prices))
    for key, items in diction.items():
        if len(key) > 10:
            price_array.append(items)
    print(max(price_array))
    return max(price_array)
