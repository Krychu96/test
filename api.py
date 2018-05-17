

import requests

GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

nr=0


def open_file(file):

    with open('workfile', 'r') as file:

        try:

            text = file.read()

        finally:

            file.close()


def split_lines(lines):

    lines = text.split('\n')

    for line in lines:

        nr+=1





    
def get_addres(line):

    params = {

        'address': line,

        'sensor': 'true',

        'region': 'pol'

    }


    req = requests.get(GOOGLE_MAPS_API_URL, params=params)

    res = req.json()


    result = res['results'][0]


    geodata = dict()

    print("Adres","nr",nr)

    geodata['lat'] = result['geometry']['location']['lat']

    geodata['long'] = result['geometry']['location']['lng']

    geodata['address'] = result['formatted_address']


    adres=('{address}. (lat, long) = ({lat}, {long})'.format(**geodata))


def print_addres(found_addres):

    found_addres = open('c:\\users\\snax\\desktop\\wyniki.txt', 'a')

    try:

        found_addres.writelines(adres)

        found_addres.write('\n')

    finally:

        found_addres.close()


    if result == True:

        print("nie udało się znaleźć adresu")

    else:

        print("udało się znaleźć adres " ,"'", line,"'" )

