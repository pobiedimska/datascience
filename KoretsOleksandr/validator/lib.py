import re

def cen_year_validator(promt):
    pattern = re.compile(r"^\d{4}$")
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

#print(cen_year_validator('input cen_year'))


def vert_other_validator(promt):
    pattern = re.compile(r"^yes|no$")
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

#print(vert_other_validator('input yes or no : '))

def borocode_validator(promt):
    pattern = re.compile(r"^[1-5]{1}$")
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

#print(borocode_validator('input borocode : '))

def boroname_validator(promt):
    pattern = re.compile(r"^[A-Z]{1}\w{1,10}$")
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

#print(boroname_validator('input boroname : '))