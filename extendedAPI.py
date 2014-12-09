import urllib2
import json
import csv

c = csv.writer(open("analysis output.csv", "wb"))

urlIncomeStatement = 'http://dev.c0l.in:5984/income_statements/_all_docs'
apiIncomeStatement = urllib2.urlopen(urlIncomeStatement)
dataIncomeStatement = json.load(apiIncomeStatement)

urlFinancialPosition = 'http://dev.c0l.in:5984/financial_positions/'
apiFinancialPosition = urllib2.urlopen(urlFinancialPosition)
dataFinancialPosition = json.load(apiFinancialPosition)


for item in dataIncomeStatement['rows']:
    url = 'http://dev.c0l.in:5984/income_statements/' + item['id']
    print url
