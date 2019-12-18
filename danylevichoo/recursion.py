data_set={
    '1':{
        "host-id":956883,
        "bed-type":"Real Bed",
        "price":85.00,
        "extra-people":5.00
        },
   '2':{
        "host-id":5177328,
        "bed-type":"Real Bed",
        "price":150.00,
        "extra-people":0.00
        },
    '3':{
        "host-id":16708587,
        "bed-type":"Real Bed",
        "price":975.00,
        "extra-people":25.00
        }
}

def rec(data_set,n=1):
    if n>len(data_set):
        return 0
    elif int(data_set[str(n)]["price"])>10 and int(data_set[str(n)]["price"])<100 :
        print(data_set[str(n)]["host-id"])
        print(data_set[str(n)]["bed-type"])
        print(data_set[str(n)]["price"])
    n=n+1
    rec(data_set,n)