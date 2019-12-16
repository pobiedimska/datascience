from lib import *

def output(attribute, ds_correct, ds_incorrect, ds_of_functions):
    print('Атрибут:', attribute)
    print('Дані правильні:', ds_correct)
    print('Дані неправильні:', ds_incorrect, '\n')

ds_correct = {'zipcode': '98119', 'street': '8th Avenue West, Seattle, WA 98119, United States', 'space': 'I hope this space will make my guests feel like they (EMAIL HIDDEN)fortable, in a great location and peaceful for an ideal getaway.', 'host_id': '1452570'}
ds_incorrect = {'zipcode': 'abc12', 'street': 'Вулиця Політехнічна, 22', 'space': 'It\'s an amazing flat.\n                  The park is near.', 'host_id': 'My host_id is: 1452570'}
ds_of_attributes = ds_correct.keys()

for i in ds_of_attributes:

    ds_of_functions = {
        '0': zipcode_validator(i),
        '1': street_validator(i),
        '2': space_validator(i),
        '3': host_id_validator(i)}

    output(i, ds_correct[i], ds_incorrect[i], ds_of_functions1[i])