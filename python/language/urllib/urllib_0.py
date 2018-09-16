import os
import urllib
#import urllib2
from bs4 import BeautifulSoup

url = "https://github.com/praveentn"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html)

imgs = soup.findAll("div", {"class":"h-card col-3 float-left pr-3"})
for img in imgs:
    imgUrl = img.a['href'].split("imgurl=")[1]
    urllib.request.urlretrieve(imgUrl, os.path.basename(imgUrl))

