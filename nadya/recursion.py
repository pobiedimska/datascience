from nadya.dataset_structure import Data
listofvar=[]#list created for finding an appropriate value(in our case max weight, when a color is red)
for key,value in Data.items():#key=item1; value = all characteristic
    for charact,charactval in value.items():#charact=size; charactval=7
        if charact == "color" and charactval=="Red":
            print(value)
            for chkey,chval in value.items():
                if chkey=="weight":
                    listofvar.append(chval)
print(max(listofvar))



