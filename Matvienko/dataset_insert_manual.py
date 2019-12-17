from dataset_structure import dataset

def insert(dataset, cen_year, horz_plant, vert_wall, sidw_raise):
    dataset[len(dataset)+1] = {"cen_year": cen_year
        , "horz_plant": horz_plant
        , "vert_wall": vert_wall
        , "sidw_raise": sidw_raise
                                 }


insert(dataset, 2006, "No", "No", "Yes")

print(dataset)

