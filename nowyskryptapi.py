import requests

GOOGLE_API = 'http://maps.googleapis.com/maps/api/geocode/json'

def get_address(address_list):
    params = {
        'address': address_list,
        'sensor': 'true',
        'region': 'pol'
    }
    r = requests.get(GOOGLE_API, params=params)
    return r.json()['results'][0]

def read_tekst_txt():
    with open ("adress.txt") as file:
        address_list=[]
        address_list=file.read_tekst_txt
        
    '''

    Funkcja ma wczytywać plik tekst txt z folderu ze skryptem
    I ma zwracać listę adresów do podania funkcji get_address
    '''
    pass

def get_coordinates(address_list):
    
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
        res = req.json()

        result = res['results'][0]

        geodata = dict()
        geodata['lat'] = result['geometry']['location']['lat']
        geodata['lng'] = result['geometry']['location']['lng']
        geodata['address'] = result['formatted_address']
        found_addresses=('{address}. (lat, long) = ({lat}, {long})'.format(**geodata))
    '''
    Funkcja ma przyjmować listę adresów
    I ma zwracać listę znalezionych koordynatów
    '''
    pass

def save_to_wyniki_txt(found_addresses):
    with open('found_addresses.txt','w') as file:
        file.write(found_addresses)

    
    '''
    Funkcja ma przyjmować listę znalezionych adresów
    I ma nic nie zwracać
    Ale ma zapisywać w pliku wyniki.txt wyniki
    '''
    pass

if __name__ == '__main__':
    address_list = read_tekst_txt()
    found_addresses = get_coordinates(address_list)
    save_to_wyniki_txt(found_addresses)
    print(len(found_addresses) == len(address_list))