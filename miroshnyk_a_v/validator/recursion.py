from miroshnyk_a_v.validator.dataset_structure import dataset


def get_sum(data,sum):
    yes = 0
    if isinstance(data,dict):
        for key,value in data.items():
            if key=="size":
                if 14 in value:
                    yes=1
            elif yes==1 and key=="quantities":
                sum=sum+value
            else:
                sum=get_sum(value,sum)
    return sum
print("Сума кількостей взуття з розміром 14: "+str(get_sum(dataset,0)))