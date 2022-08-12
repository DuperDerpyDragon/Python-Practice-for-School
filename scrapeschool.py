from urllib.request import urlopen
from html.parser import HTMLParser
import requests

schoolUrl = "https://bellbirdparkssc.eq.edu.au/our-school"
schoolUrl = "https://bellbirdparkssc.eq.edu.au/our-school/our-staff"
page = urlopen(schoolUrl)

urlCoding = page.readText()
print(urlCoding)
exit()

html = urlCoding.decode("utf-8")

readText = True
text = []
class Parser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    global readText
    tag = tag.lower()
    readText = tag != 'script' and tag != 'style' and tag != 'meta'

    if(readText):
        print(tag)

    readText = True
  def handle_endtag(self, tag):
    global readText
    readText = True
  def handle_data(self, data):
    global text
    if(readText):
        text.append(data)

parser = Parser()
parser.feed(html)

print(text)
