import re


def ean_validator():
    ean = input('Введіть значення унікального штрих-коду: ')
    if bool(re.match('^[0-9]{1}\.[0-9]{5}E\+[0-9]{2}$', ean)):
        pass
    else:
        print('Error')
        return ean_validator()
    return ean



def keys_validator():
    keys = input('Введіть унікальні ключові слова, вирази та відповідні їм коди: ')
    if bool(re.match('^(([a-z]+(\,){1}(\s){1}[0-9]{12}){1}((\s){1}(\/){1}(\s){1}[a-z]+(\,){1}(\s){1}[0-9]{12})*)$', keys)):
        pass
    else:
        print('Error')
        return keys_validator()
    return keys



def manufacturer_validator():
    manufacturer = input('Введіть назву виробника: ')
    if bool(re.match('^(([A-Z]+([a-z]*)((\')?([a-z]*)(\.)?[a-z]*)(\s)?)*)$', manufacturer)):
        pass
    else:
        print('Error')
        return manufacturer_validator()
    return manufacturer


def brand_validator():
    brand = input('Введіть назву бренда: ')
    if bool(re.match('^(([A-Z]+([a-z]*)((\')?([a-z]*)(\.)?[a-z]*)(\s)?)*)$', brand)):
        pass
    else:
        print('Error')
        return brand_validator()
    return brand


