from oliinykao.validator.lib import *
id = input("Введіть id - ")
print(id_validator(id).group())
brand = input("Введіть brand - ")
print(brand_validator(brand).group())
colors = input("Введіть colors - ")
print(colors_validator(colors).group())
flavors = input("Введіть flavors - ")
print(flavors_validator(flavors).group())