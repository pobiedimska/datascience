import MykhailenkoYaroslava_work.validator.lib
# import MykhailenkoYaroslava_work.dataset_insert_manual
print(MykhailenkoYaroslava_work.validator.lib.status_validator('good'))
print(MykhailenkoYaroslava_work.validator.lib.status_validator('notgood'))
print(MykhailenkoYaroslava_work.validator.lib.horz_plant_validator('yes'))
print(MykhailenkoYaroslava_work.validator.lib.horz_plant_validator('notyes'))
print(MykhailenkoYaroslava_work.validator.lib.zip_city_validator('Staten Island'))
print(MykhailenkoYaroslava_work.validator.lib.zip_city_validator('67'))
print(MykhailenkoYaroslava_work.validator.lib.boroname_validator("5"))
print(MykhailenkoYaroslava_work.validator.lib.boroname_validator("7"))
