from bs4 import BeautifulSoup

html='<span itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress"><span itemprop="streetAddress">3023 S Lloyd Ave</span> <br><span itemprop="addressLocality">Chicago</span> <span itemprop="addressRegion">Illinois</span> <span itemprop="postalCode">60608</span></span>'
soup = BeautifulSoup(html, features="lxml")

spans = soup.select("span span")
addrs = []
for s in spans:
   addrs.append(s.text)
print(addrs)