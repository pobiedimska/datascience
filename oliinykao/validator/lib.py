import re
def id_validator(id):
    return re.match("^AVpe\_.{15}$", id)

def brand_validator(brand):
    return re.match("^\w*(\s\w*)*$", brand)

def colors_validator(colors):
    return re.match("^[A-Za-z]\w*(\s\w*)$", colors)

def flavors_validator(flavors):
    return re.match("^[A-Z]\w*(\s\w*)*$")