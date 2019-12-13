from KoretsOleksandr.dataset_structure import dataset

def recursin_func(information,help_var):

    if len(information)>=1:
        if information[0] == 'Bronx':
            print(information[0])
            help_var = help_var + 1
            return recursin_func(information[1:],help_var)
        else:
            return recursin_func(information[1:],help_var)
    return help_var

print(recursin_func(dataset['borocode'],0))