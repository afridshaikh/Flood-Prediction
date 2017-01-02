import requests
import csv
from bs4 import BeautifulSoup
i = 0
url = 'http://www.imdmumbai.gov.in/scripts/detail.asp?releaseid=E2016RW'

def getdata(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find_all('table', {'width': '730'})
        if len(table) != 0:
            row1 = table[0].find_all('tr')[1]
            row2 = table[0].find_all('tr')[2]
            date = row1.find_all('td')[0].text.encode('ascii')
            time = row1.find_all('td')[1].text.encode('ascii')
            desc = row2.find_all('td')[0].text.encode('ascii')
            date = date.replace('Date : ','')
        elif len(table) == 0:
            table = soup.find_all('table', {'id': 'table1'})[0]
            rows = table.find_all('tr')
            date_time = rows[0].find_all('td')[0].text.encode('latin-1')
            date_time = date_time.replace('\xa0', '')
            #date_time = date_time.replace('\n', '').replace('\r','').replace('\t','')
            date = date_time[date_time.index('Da'):date_time.index('Ti')]
            date = date.replace('Date:','').replace(' ','')
            date = date.replace('-','/').replace('\n', '').replace('\r','').replace('\t','')
            time = date_time[date_time.index('Ti'):date_time.index('HRS')+3].replace('\n', '').replace('\r','').replace('\t','')
            if 'IST' in date_time:
                desc = date_time[date_time.index('IST')+3:].replace('\n', '').replace('\r','').replace('\t','')
            else :
                desc = date_time[date_time.index('HRS')+3:].replace('\n', '').replace('\r','').replace('\t','')
        else :
            print 'Something went wrong'
    
        f = open('E:\Projects\Flood-Prediction\data\warn_data2016.csv', 'ab')
        writer = csv.writer(f, delimiter=',')
        writer.writerow([date,time,desc])
        f.close()
    except Exception as e:
        print e, url


while i < 354:
    i = i + 1
    getdata(url + str(i))
    print i

    
    
