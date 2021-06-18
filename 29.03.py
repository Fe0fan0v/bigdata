import requests
from io import BytesIO
from PIL import Image

server = 'http://static-maps.yandex.ru/1.x/'
server_address = 'http://geocode-maps.yandex.ru/1.x/'

address = {'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
           'geocode': input(),
           'format': 'json'}
coords = requests.get(server_address, address).json()
coords = coords['response']['GeoObjectCollection'] \
    ['featureMember'][0]['GeoObject']['Point']['pos'].replace(' ', ',')

point = {'ll': coords,
         'spn': '0.002,0.002',
         'l': 'sat,skl'}

resp = requests.get(server, point).content
img_b = BytesIO(resp)
Image.open(img_b).save('map.png')
