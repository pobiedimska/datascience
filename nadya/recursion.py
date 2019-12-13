from nadya.dataset_structure import Data
counting=list(Data.items())
length=len(counting)
K=0
N=1
listofvar=[]#list created for finding an appropriate value(in our case max weight, when a color is red)
def recursion(data, tamplate_key, tamplate_val, K,N):
    for key,value in data.items():
        for seckey,secvalue in value.items():
            if seckey==tamplate_key and secvalue==tamplate_val:
                if K==length:
                    return listofvar.append(value.get("weight"))
                else:
                    return listofvar.append(value.get("weight")), recursion(dict(counting[K:N]), "color", "Red",K+1,N+1)
            else:
                return recursion(dict(counting[K:N]),"color","Red",K+1,N=1)
recursion(dict(counting[K:N]),"color","Red",K,N)
print("Maximum weight for red items is",max(listofvar))


