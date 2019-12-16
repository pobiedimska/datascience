import re
re_provider_id = re.compile("^[+]?\d{6}?")
re_agency_name = re.compile("^(([a-wA-W]+)\s{0,1})+")
re_average_hcc_scor = re.compile("^([-+]?\d+\.?\d*\s*)+$")
re_percent_of_beneficiaries_with_asthma = re.compile("^\d+$")
def provider_id_validator(regexp):
    value = input("Enter provider id:\n")
    while not regexp.match(value) or len(value) > 6:
        value = input("Must consist only of numbers (exactly six).\nTry again:\n")

def agency_name_validator(regexp):
    value = input("Enter the agency name:\n")
    while not regexp.match(value):
        value = input("Incorrect name. Try again:\n").upper()

def average_hcc_score_validator(regexp):
    value = input("Enter average hcc score:\n")
    while not regexp.match(value):
        value = input("Must consist only numbers(integer or float):\n")

def percent_of_beneficiaries_with_asthma_validator(regexp):
    value = input("Enter percent of beneficiaries with asthma:\n")
    while not regexp.match(value) or int(value) > 100:
        value = input("Must consist only integer value(less than 100):\n")
