from nadya.dataset_structure import Data
counting=list(Data.items())
length=len(counting)
first_index=0
second_index=1
listofvar=[]#list created for finding an appropriate value(in our case max weight, when a color is red)
def recursion(data, tamplate_key, tamplate_val, first_index,second_index):
    for key,value in data.items():
        for seckey,secvalue in value.items():
            if seckey==tamplate_key and secvalue==tamplate_val:
                if first_index==length:
                    return listofvar.append(value.get("weight"))
                else:
                    return listofvar.append(value.get("weight")), recursion(dict(counting[first_index:second_index]), "color", "Red",first_index+1,second_index+1)
            else:
                return recursion(dict(counting[first_index:second_index]),"color","Red",first_index+1,second_index=1)
recursion(dict(counting[first_index:second_index]),"color","Red",first_index,second_index)
print("Maximum weight for red items is",max(listofvar))

#функція виводить максимальне значення ваги, для всіх продуктів червоного кольору
