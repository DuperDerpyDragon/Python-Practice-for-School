from urllib.request import urlopen

schoolUrl = "https://bellbirdparkssc.eq.edu.au/our-school"
page = urlopen(schoolUrl)

urlCoding = page.read()
html = urlCoding.decode("utf-8")

print(html)