import requests
from bs4 import BeautifulSoup
import csv
import string
url = 'http://www.imdmumbai.gov.in/scripts/detail.asp?releaseid=E2011WD'
i = 0

def getdata(url):
  try:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find_all('table', {'cellspacing': '0', 'cellpadding': '0', 'align': 'top', 'width': '100%', 'border': '1'})[0].find_all('tr')
    a, b = [], []
    date = rows[2].find_all("td")[7].text
    date = date.replace('  Since ','')
    b.append([date])
    for row in rows:
      if len(row) == 12:
        l = []
        for cell in row.find_all('td'):
          l.append(cell.text)
        b.append(l)
    f = open('E:\Projects\Flood-Prediction\data\data2011.csv', 'ab')
    b.append(date)
    writer = csv.writer(f, delimiter=',')
    writer.writerow(b)
    f.close()
  except:
    pass

while i < 361:
  i += 1
  getdata(url + str(i))
