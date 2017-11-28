import json
import re
import requests
import shutil
import os

URL_PATTERN = f'https://\w+\.cloudfront\.net/\w+/book/pages/([0-9a-z-]+)\?(\w+=\w+&)*(\w+=\w+)'

with open('input.json') as f:
	obj = json.load(f)

# extract datetime of request and URL of image
urls = [ 
	( entry['startedDateTime'], entry['request']['url'] )
for entry in obj['log']['entries'] if re.match(URL_PATTERN, entry['request']['url'])]
urls.sort(key=lambda x: x[0])

# make sure /images exists
if not os.path.exists('images'):
    os.makedirs('images')

def dl_image(url):
	response = requests.get(url[1], stream=True)
	filename = 'images/' + url[0].replace(':', '-') + '.jpg'
	with open(filename, 'wb') as f:
		shutil.copyfileobj(response.raw, f)
	del response

for url in urls:
	dl_image(url)
