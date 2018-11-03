'''
Write a program that goes to a photo sharing site like Flickr or Imgur,
searches for a category of photos, then downloads all the resulting images.
'''

import requests, bs4, re
res = requests.get('https://imgur.com/search?q=sports')
res.raise_for_status()
imagesSoup = bs4.BeautifulSoup(res.text, "html.parser")
print(imagesSoup.select('img'))