import urllib2
import json

print "Hello and welcome to Currency Converter v0.1"

pounds = input("amount you wish to exchange: ")
url = "http://rate-exchange.appspot.com/currency?from=GBP&to=EUR"
if pounds.isdigit():
    print total
else:
    print "Please, use numeric input, we are not able to convert letters into"
    "money. (But that would be awesome!)"
    
response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))
rates = data ['rate']
total = pounds * rates
