from bs4 import BeautifulSoup
import urllib3
import re

http = urllib3.PoolManager()
url = "http://dev.stephendiehl.com/fun/"
response = http.request("GET", url)
soup = BeautifulSoup(response.data)
pos = []
for x in range(len(url)):
    if "." is url[x]:
        pos.append(x)
domain = url[pos[0]+1:pos[1]]
for link in soup.findAll('a', attrs = {'href': re.compile("^http://")}):
    if domain in link.get("href"):
        print (link.get("href"))

