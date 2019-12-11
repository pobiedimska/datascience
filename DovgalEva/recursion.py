from DovgalEva.dataset_structure import dataset

def recursion(data):
    if len(data) == 0:
        return 0

    condition = 0
    for key, value in data[0].items():
        if key == 'city' and value == 'IRWINDALE':
            condition +=1
        elif key == 'total_episodes_non_lupa' and value > 1000:
            condition +=1
        else: continue
    if condition == 2:
        print(data[0].get('provider_id'))
        print(data[0].get('zip_code'))
        print(data[0].get('city'))

    data = data[1:]
    recursion(data)


recursion(dataset)