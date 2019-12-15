import re

def host_id_validator(message):
    host_id = input(message)
    if bool(re.match(r'^\d+$', host_id)):
        return host_id
    else:
        print("Expression is invalid! Try again")
        return host_id_validator(message)

def beds_validator(message):
    beds = input(message)
    if bool(re.match(r'^\d+$', beds)):
        return beds
    else:
        print("Expression is invalid! Try again")
        return beds_validator(message)

def number_reviews_validator(message):
    number_reviews = input(message)
    if bool(re.match(r'^\d+$', number_reviews)):
        return number_reviews
    else:
        print("Expression is invalid! Try again")
        return number_reviews_validator(message)

def country_validator(message):
    country = input(message)
    if bool(re.match(r'^([U][n][i][t][e][d] [S][t][a][t][e][s]){1}$', country)):
        return country
    else:
        print("Expression is invalid! Try again")
        return country_validator(message)