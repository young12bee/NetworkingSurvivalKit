#!/python33/python
#Python 3 Example of how to use https://macvendors.co to lookup vendor from mac address
print ("Content-Type: text/html\n")

# import urllib.request as urllib2
import urllib2
import json
import codecs

#API base url,you can also use https if you need
url = "http://macvendors.co/api/"
#Mac address to lookup vendor from
# mac_address = "BC:92:6B:A0:00:01"
mac_address = "48-45-20-A6-1A-08"

request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"})
# print 'request: ',request
response = urllib2.urlopen( request )
# print 'response: ',response
#Fix: json object must be str, not 'bytes'
reader = codecs.getreader("utf-8")
# print 'reader: ',reader
obj = json.load(reader(response))
# print 'obj: ',obj

#Print company name
print (obj['result']['company']);
# print (obj['result']['company']+"<br/>");
#print company address
print (obj['result']['address']);
