import urllib2
import json

def locu_search():
    api_key = 'f3643d864d48e74de6c24a77aadd83e42ed39507'
    country = raw_input("Please enter country u want to look up: ")
    print ""
    city = raw_input("Please enter city u want to look up: ")
    print ""
    print "Printing out results for: " + country + ', ' + city
    print ""
    url = 'https://api.locu.com/v1_0/venue/search/?locality=' + city.replace(' ', '%20') + '&country=' + country.replace(' ', '%20') + '&api_key=' + api_key + '&category=restaurant'
    api = urllib2.urlopen(url)
    data = json.load(api)
    for item in data['objects']:
        print 'Restaurant name: ' + str(item['name'])
        print 'Restaurant phone: ' + str(item['phone'])
        print ''

locu_search()
