def recursion(dataset,n=0):
    while len(dataset.keys())!=n:
        id=list(dataset.keys())[n]
        neighbourhood = dataset[id]["neighbourhood"]
        state = dataset[id]["state"]
        market = dataset[id]["market"]
        country = dataset[id]["country"]
        if state == "WA" or neighbourhood == "Ballord":
            print("\nID:"+str(id) + "\nMarket:"+str(market)+"\nCountry:" + str(country)+"\nState:"+str(state))
        return recursion(dataset,n+1)

dataset={
    "7421966":{
        "neighbourhood":"Queen Anne",
        "state":"WA",
        "market":"Seattle",
        "country":"United States"
    },
    "1266459":{
        "neighbourhood":"Ballard",
        "state":"WA",
        "market":"Seattle",
        "country":"United States"
    },
    "6202214":{
        "neighbourhood":"Wallingford",
        "state":"WA",
        "market":"Seattle",
        "country":"United States"
    }

}
recursion(dataset)
