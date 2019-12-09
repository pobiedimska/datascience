from miroshnyk_a_v.validator.dataset_structure import dataset
sum=0

def get_sum(data):
    yes = 0
    for key,value in data.items():
        print(key)
        if key=="size":
            if value==14:
                yes=1
        elif yes==1 and key=="quantities":
            sum=+value
        else:
            get_sum(value)
    return sum
print(get_sum(dataset))