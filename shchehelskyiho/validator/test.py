from lib import *

if zipcode_validator('98119'):
    print('Дані правильні')
else: print('Дані неправильні')

if street_validator('8th Avenue West, Seattle, WA 98119, United States'):
    print('Дані правильні')
else: print('Дані неправильні')

if space_validator('I hope this space will make my guests feel like they (EMAIL HIDDEN)fortable, in a great location and peaceful for an ideal getaway.'):
    print('Дані правильні')
else: print('Дані неправильні')

if host_id_validator('1452570'):
    print('Дані правильні')
else: print('Дані неправильні')