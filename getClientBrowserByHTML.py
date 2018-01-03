import urllib2

# Derive from Request class and override get_method to allow a HEAD request.
class HeadRequest(urllib2.Request):
    def get_method(self):
        return "HEAD"

myurl = 'https://www.google.com'
request = HeadRequest(myurl)

try:
    response = urllib2.urlopen(request)
    response_headers = response.info()
    response_geturl = response.geturl()
    response_getcode = response.getcode()

    # This will just display all the dictionary key-value pairs.  Replace this
    # line with something useful.
    response_headers.dict
    # print (response_headers.dict)
    print (response_headers)
    print 'URL = ', (response_geturl)
    print ' Status Code of Request = ', (response_getcode)

except urllib2.HTTPError, e:
    # Prints the HTTP Status code of the response but only if there was a
    # problem.
    print ("Error code: %s" % e.code)
