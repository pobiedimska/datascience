def recursion(dataset):
    for id in dataset.keys():
        street = dataset[id]['street']
        city = dataset[id]['city']
        price = dataset[id]['price']
        country_code = dataset[id]['country_code']
        if price > 15 and price < 100 and country_code == 'US':
            print('ID: '+ id +'\nStreet: ' + street + '\nCity: ' + city + '\nPrice: ' + price + '\n')