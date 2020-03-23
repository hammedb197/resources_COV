import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
# import bs4/


# print(help(bs4))
url = "http://covid19.ncdc.gov.ng/"
 
def get_nigeria(url):
    request_ = requests.get(url).text
    soup = bs(request_, 'html.parser')
    tabel_ = soup.find('table', id='custom3').prettify()
    data = pd.read_html(tabel_)
    data = data[0]
    data = pd.concat([data[:1], data[1:]], axis=0)
    return data.head()
     
print(get_nigeria(url))