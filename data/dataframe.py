import requests
from bs4 import BeautifulSoup
import csv
import string
import pandas as pd
import datetime
i = 0
url = 'http://www.imdmumbai.gov.in/scripts/detail.asp?releaseid=E2010WD'
def getdate(datestr):
    date = datetime.datetime.strptime(datestr, '%B %d,%Y').strftime('%d%m%Y')
    return date

def getdata(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        rows = soup.find_all('table', {'cellspacing': '0', 'cellpadding': '0', 'width': '700', 'border': '0'})[0].find_all('tr')
        a,b = [],[]
        date = rows[0].text.encode("ascii")
        date = date[62:len(date)-1]
        date = getdate(date)
        filepath = 'E:\Projects\Flood-Prediction\data\RainFallData\data2010\\' + date + '.csv'
        for row in rows:
            if len(row) == 25:
                a = []
                for cell in row.find_all('td'):
                    a.append(cell.text.replace('\xa0','').encode("ascii"))
                b.append(a)
        df = pd.DataFrame(b)
        print date
        df.to_csv(filepath, sep=',')
                
    except Exception as e:
        print e

    
while i < 182:
    i += 1
    getdata(url + str(i))
    print i, '\n'


            

