def recursion(dataset):
    for provider_id in dataset.keys():
        agency_name = dataset[provider_id]['agency_name']
        total_lupa_edisodes = int(dataset[provider_id]['total_lupa_edisodes'])
        avarage_age = int(dataset[provider_id]['avarage_age'])
        
        if total_lupa_edisodes > 10 or avarage_age > 40:
            print('Agency_name:' + str(agency_name) + '\nTotal_lupa_edisodes:' + str(total_lupa_edisodes))
