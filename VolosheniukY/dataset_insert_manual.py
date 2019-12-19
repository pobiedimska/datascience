from dataset_structure import data_set


def add_data(name, city, country, country_code):
    data_set.update({
        name: {
            "city": city,
            "country": country,
            "country_code": country_code
        }
    })
    return data_set


data_set = add_data('Royal Apartment of Jordan 3', 'Seattle', 'United States', 'US')
print(data_set)

