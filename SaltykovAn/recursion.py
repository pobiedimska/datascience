def shows_parameters(dataset):

  if not len(dataset):
    return False
  else:
    if dataset[0]['beds']>2 or dataset[0]['price']>100:
      for k in dataset[0].keys():
        if k != 'beds':
          print(dataset[0][k])
      print('\n')
    return shows_parameters(dataset[1:])

shows_parameters(dataset)
