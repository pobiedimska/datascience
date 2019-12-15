import re
def cb_num_validator(cb_num):
    while bool(re.match(r"^\d+$",cb_num)):
        return cb_num

def zipcode_validator(zipcode):
    while bool(re.match(r"^\d+$", zipcode)):
        return zipcode
def wire_2nd_validator(wire_2nd):
    while bool(re.match(r"(False)|(True)", wire_2nd)):
        return wire_2nd
def spc_latin_validator(spc_latin):
    while bool(re.match(r"[A-Z]+(\s)[A-Z]+", spc_latin)):
        return spc_latin
