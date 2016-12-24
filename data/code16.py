import csv
import requests
import string
from bs4 import BeautifulSoup
i = 0
url = "http://www.imdmumbai.gov.in/scripts/detail.asp?releaseid=E2016RF"

def getdata(str):
    try:
        r = requests.get(str)
        soup = BeautifulSoup(r.content)
        table = soup.find_all("table")[6]
        date = table.find_all("tr")[1].find_all("td")[0].text
        date = date.replace("\n","")
        date = date.replace("\t","")
        date = date.replace("\r","")
        date = date.replace(" ","")
        date = date.replace("%DEPARTUREOFRAINFALLON","")
        date = date.replace("DATE:","")
        mumbai_city = table.find_all("tr")[10]
        city_rain = mumbai_city.find_all("td")[1].text
        city_rain = city_rain.replace("\n\n","")
        city_rain = float(city_rain)
        mumbai_sub = table.find_all("tr")[11]
        sub_rain = mumbai_sub.find_all("td")[1].text
        sub_rain = sub_rain.replace("\n\n","")
        sub_rain = float(sub_rain)
        city = open('E:\ProjectFlood\data\mumbai_city16.csv', 'ab')
        city_writer = csv.writer(city, delimiter=',')
        city_writer.writerow([date, city_rain])
        city.close()
        sub = open('E:\ProjectFlood\data\mumbai_sub16.csv', 'ab')
        sub_writer = csv.writer(sub, delimiter=',')
        sub_writer.writerow([date, sub_rain])
        sub.close()
    except:
        pass
    return

while i<=158:
    i=i+1
    getdata( url + str(i))
