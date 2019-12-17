from PindaMV.dataset_structure import dataset
print(dataset)

count = 0
sum_confl = 0
len_dataset = len(dataset.keys())
def confl_count(dataset, sum_confl,count,len_dataset):
    value = dataset.popitem()
    dataset.update({value[0]: value[1]})
    if dataset[value[0]]['cen_year'] == 2006:
        if dataset[value[0]]['inf_other'] == 'Yes':
            sum_confl+=1
    dataset.pop(value[0])
    count+=1
    if count >= len_dataset:
        return sum_confl
    else:
        return confl_count(dataset, sum_confl,count,len_dataset)


sum = confl_count(dataset, sum_confl,count,len_dataset)
print(sum)

