import requests
nr=0
plik = open('c:\\users\\snax\\desktop\\tekst.txt', 'r')
try:
    tekst = plik.read()
finally:
    plik.close()

lines = tekst.split('\n')
for line in lines:
    nr+=1



    GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

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
    geodata['szerokość'] = result['geometry']['location']['lat']
    geodata['długość'] = result['geometry']['location']['lng']
    geodata['address'] = result['formatted_address']

    print('{address}. (szerokość, długość) = ({szerokość}, {długość})'.format(**geodata))

    if result == True:
        print("nie udało się znaleźć adresu")
    else:
        print("udało się znaleźć adres " ,"'", line,"'" )

