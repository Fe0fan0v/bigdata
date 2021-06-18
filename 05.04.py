import requests
from PIL import Image
import io


KEY = 'JBuGtYcdod8udN03Io2XfuD5FejXbhYvwWUkwE2y'
SERVER = 'https://api.nasa.gov/mars-photos/api/v1/rovers/'


params = {'api_key': KEY}
response = requests.get(SERVER, params).json()
rovers = []
for rover in response['rovers']:
    rovers.append(rover['name'])
sol = response['rovers'][-1]['max_sol']
photo_params = {'api_key': KEY, 'sol': sol}
photo = requests.get(f'{SERVER}{rovers[-1]}/photos', photo_params).json()
count = 1
for f in photo['photos']:
    img = f['img_src']
    image_bytes = requests.get(img).content
    image = Image.open(io.BytesIO(image_bytes))
    image.save(f'images/img{count}.jpg')
    count += 1
