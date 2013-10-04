import urllib2

def read_url(self, url):
    request = urllib2.Request(url)
    response = None
    response_string = ''
    try:
        response = urllib2.urlopen(request, timeout=12000)
        response_string = response.read()
    except Exception, err:
        print err
