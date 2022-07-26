from bs4 import bs
import urllib2

url = "https://bellbirdparkssc.eq.edu.au/our-school"
html = urllib2.urlopen(url).read()
soup = bs(html)
for word in soup.text:
    print(soup.text)
