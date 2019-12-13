def recurcion(dataset):
    for host_id in dataset.keys():
        if "bedrooms">=2 or roomtype == "Private room":
            print("Host ID: "+str(host_id)+"\nroomtype: "+str(room_type)+"\ncountry: "+str(country))


dataset = {
    "956883":
        {
            "room_type":"Entire home/apt",
            "bedrooms":"1",
            "country":"United States"

        },
    "2166277":
        {
            "room_type":"Private room",
            "bedrooms":"1",
            "country":"United States",
        },
    "25906186":
        {
            "room_type":"Entire home/apt",
            "bedrooms":"4",
            "country":"United States"
        }
     }

print(recurcion(dataset))