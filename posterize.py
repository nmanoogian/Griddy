import urllib, urllib2
import os
import simplejson
import sys, time
import re


def getImageURL(query):
    url = ('https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' + urllib.quote_plus(query) + '&userip=INSERT-USER-IP')
    request = urllib2.Request(url, None, {'Referer': 'http://google.com'})
    response = urllib2.urlopen(request)
    results = simplejson.load(response)
    return results['responseData']['results'][0]['unescapedUrl']

file_ext = ["mkv", "avi", "mp4"]


print """
<html>
<head><title>Movies!</title></head>
<body>
"""


for line in sys.stdin:
    BASE_FILE = line.strip().split("/")[-1]
    for ext in file_ext:
        if ext in BASE_FILE:
            ICAPTITLE = re.sub("\.", "", BASE_FILE.split(ext)[0]).strip()
            os.system("wget -O " + ICAPTITLE + ".jpg " + getImageURL(ICAPTITLE))
            print "<img height=350px src=" + ICAPTITLE + ".jpg />"
            break
            
    time.sleep(1.5)

print """
</body>
</html>
"""