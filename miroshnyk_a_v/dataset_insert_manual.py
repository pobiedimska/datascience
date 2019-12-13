from miroshnyk_a_v.dataset_structure import dataset
for val in dataset.values():
     val.update({
    'Handcrafted Alpaca Blenk\'Purple Charisma\' Sweater (Peru)':{
         'sizes':[14,15],
         'quantities':24,
         'reviews':"Not bad"}})
print(dataset)