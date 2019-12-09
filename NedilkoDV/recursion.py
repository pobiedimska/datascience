dataset={'AVpe__eOilAPnD_xSt-H1':{
                                'count': 15,
                                'key': 'handmade',
                                'brand':'Shoes4youth1'},

        'AVpe__eOilAPnD_xSt-H2':{
                                'count': 10,
                                'key': 'handmade',
                                'brand':'NovicaShoes'},


        'AVpe__eOilAPnD_xSt-H3':{
                                'count': 95,
                                'key': 'handmade',
                                'brand':'Novica'

            }

}



def recursion(dict,n=0):
       keys1= dict.keys()
       print(keys1)
       keysList1=list(keys1)
       key1=keysList1[n]
       print(key1)
       l=dict.pop(key1)
        n+=1
       return

print(recursion(dataset))