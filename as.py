import urllib.request
from bs4 import BeautifulSoup
url = "http://www.imcshop.com/"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
soup = BeautifulSoup(response, "html.parser")
print (response.read().decode('utf-8')) 

result = soup.find_all("a")
print(result)