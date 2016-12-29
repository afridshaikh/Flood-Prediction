import requests
from bs4 import BeautifulSoup
import csv
import string
i = 0
url = 'http://www.imdmumbai.gov.in/scripts/detail.asp?releaseid=E2012WD'
def getdate(datestr):
    month = 0
    mon = datestr[0] + datestr[1] + datestr[2]
    mon = mon.lower()
    if mon == 'jan':
        month = '01'
    elif mon == 'feb':
        month = '02'
    elif mon == 'mar':
        month = '03'
    elif mon == 'apr':
        month = '04'
    elif mon == 'may':
        month = '05'
    elif mon == 'jun':
        month = '06'
    elif mon == 'jul':
        month = '07'
    elif mon == 'aug':
        month = '08'
    elif mon == 'sep':
        month = '09'
    elif mon == 'oct':
        month = '10'
    elif mon == 'nov':
        month = '11'
    elif mon == 'dec':
        month = '12'
    else:
        pass
    day = datestr[datestr.index(' ')+1 : datestr.index(',')]
    year = datestr[len(datestr)-4: len(datestr)]
    date = day + '/' + month + '/' + year
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
        f = open('E:\Projects\Flood-Prediction\data\data2012.csv', 'ab')
        writer = csv.writer(f, delimiter=',')
        writer.writerow(b)
        f.close()
    except:
        print '\n\n\n Errrorrororororororoor' + date + '\n\n\n'

    
while i < 60:
    i += 1
    getdata(url + str(i))
    print i, '\n'
            

