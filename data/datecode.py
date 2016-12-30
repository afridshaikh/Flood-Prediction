import requests
from bs4 import BeautifulSoup
import csv
import string
import datetime
i = 377
url = 'http://www.imdmumbai.gov.in/scripts/detail.asp?releaseid=E2016WD'
def getdate(datestr):
    date = datetime.datetime.strptime(datestr, '%B %d,%Y').strftime('%d/%m/%Y')
    return date

def getdata(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        rows = soup.find_all('table', {'cellspacing': '0', 'cellpadding': '0', 'align': 'top', 'width': '100%', 'border': '1'})[0].find_all('tr')
        a, b = [], []
        date = rows[0].text.encode("ascii")
        date = date[62:len(date)-1]
        date = getdate(date)
        for row in rows:
            if len(row) == 12:
                a = []
                a.append(date)
                for cell in row.find_all('td'):
                    a.append(cell.text.encode("ascii"))
                b.append(a)
        f = open('E:\Projects\Flood-Prediction\data\data2016.csv', 'ab')
        writer = csv.writer(f, delimiter=',')
        writer.writerow(b)
        f.close()
    except Exception as e:
        print e

    
while i < 378:
    i += 1
    getdata(url + str(i))
    print i, '\n'
            

