import urllib2
import unirest
import json

api = unirest.get("https://tagdef.p.mashape.com/one.{hastag}.json", headers={"X-Mashape-Key": "GrjE1PO9pdmshDpZsR9eQK4TXrj2p11QRhzjsnTnxy2h0REbBW"})
data = json.load(api)

print data
