dataset = {
    'PLATANUS ACERIFOLIA': {'status': 'good',
                            'wire_htap': 'Yes',
                            'borocode': 2},
    'ULMUS SPECIES' : {'status': 'good',
                       'wire_htap': 'No',
                       'borocode': 4},
    'GLEDITSIA TRIACANTHOS' : {'status':
                                   'excellent',
                               'wire_htap': 'No',
                               'borocode': 1}
}


# def get_all_good_status (datase):
#     counter = 1
#     key = list(dataset)[0]
#     if dataset[key]['status'] == 'good':
#         counter += 1
#     dataset.pop(key)
#     while len(dataset)>0:
#         get_all_good_status(dataset)
#     return counter
#
# print(get_all_good_status(dataset))
