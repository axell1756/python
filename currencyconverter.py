
import urllib2
import json

print "Hello and welcome to Currency Converter v0.1 (GPB to EUR)"    
url = "http://rate-exchange.appspot.com/currency?from=GBP&to=EUR"
response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))
rates = data ['rate']
rates = int()
pounds = raw_input('amount you wish to exchange: ')
total = pounds * rates

if pounds > 0 and not pounds.isalpha():
    print total
else:
    print "Please, use numeric input, we are not able to convert letters into money. (But that would be awesome!)"
def restart():
    if answer == "y" or "yes":
        pounds = raw_input('amount you wish to exchange: ')
    else:
        quit

answer = raw_input('Do u want to convert some more? "Y" or "N"').lower
restart();
