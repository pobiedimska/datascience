from pobiedimskasi.dataset_structure import dataset

def recursion(dataset):
    for provider_id in dataset.keys():
        state = dataset[provider_id]['state']
        percent_of_beneficiaries_with_depression = int(dataset[provider_id]['percent_of_beneficiaries_with_depression'])
        percent_of_beneficiaries_with_hyperlipidemia = int(dataset[provider_id]['percent_of_beneficiaries_with_hyperlipidemia'])
        condition1 = percent_of_beneficiaries_with_depression > 50
        condition2 = percent_of_beneficiaries_with_hyperlipidemia > 30
        if condition1 or condition2:
            print('Provider ID: '+str(provider_id +'\nState: ' + state+'\n'))
            
recursion(dataset)
