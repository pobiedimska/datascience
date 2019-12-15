# Побудувати рекурсивну функцію, що друкує кількісь ключив за умови, що назва ключа більш трійки
dataset = {
        "Boots": {
            "id": "1234qw_er23",
            "prices.offer": {46, 567, 453},
            "size": {41, 42, 43, 44}
        },
        "Hills": {
            "id": "AVpe__eOilAPnD_xSt",
            "prices.offer": {478, 57, 4531},
            "size": {41, 42, 44}
        },
        "Shoes": {
            "id": "AVpe__eOilAPnD_t-H",
            "prices.offer": {46, 567, 453},
            "size": {41, 42, 43, 44}
        },
}
i = 0
def recursion(dataset, i):
    N = list(dataset.keys())
    if len(dataset) > i:
        if len(N[i]) > 3:
            return recursion(dataset, i-1) + dataset[N[i]].get('name')
    else:
        return 0
        # if dict(dataset[id]) == True:
        #     name = dataset[id[name]]
        #     if len(id[name])>3:
        #         return i+1
        #     else:
        #         return i+0
        # if dict(dataset[id]) == False:
        #     return i+0

print(recursion(dataset, i))