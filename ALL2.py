import requests
import urllib2
import json

url = 'http://dev.c0l.in:8888/'
api = urllib2.urlopen(url)
data = json.load(api)
print data

for item in data['sector:technology'], data['company']:
    print item['name']
    
