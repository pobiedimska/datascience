def recursion(dataset):
    for provider_id in dataset.keys():
        city = dataset[provider_id]['city']
        percent_cancer = int(dataset[provider_id]['percent_of_beneficiaries_with_cancer'])
        percent__diabetes = int(dataset[provider_id]['percent_of_beneficiaries_with_diabetes'])
        if (percent_cancer > 10) or (percent__diabetes > 50) or (percent_cancer>5 and percent__diabetes> 20):
            print('\n\nProvider ID: '+str(provider_id)
                  +'\nCity: ' + city
                  +'\nPercent of beneficiaries with cancer: '+str(percent_cancer)+'\n')