import csv
import requests
import string
from bs4 import BeautifulSoup
#r = requests.get('http://www.imdmumbai.gov.in/scripts/detail.asp?releaseid=E2016RF19')
r = requests.get('http://www.imdmumbai.gov.in/scripts/detail.asp?releaseid=E2014RF77')
#r = requests.get('http://www.imdmumbai.gov.in/scripts/detail.asp?releaseid=E2010RF1')
soup = BeautifulSoup(r.content)
table = soup.find_all("table")[6]

date = table.find_all("tr")[1].find_all("td")[0].text
#date = date.replace("\n","")
#date = date.replace("\t","")
#date = date.replace("\r","")
#date = date.replace(" ","")
#date = date.replace("%DEPARTUREOFRAINFALLON","")
#date = date.replace("DATE:","")

mumbai_city = table.find_all("tr")[10]
city_rain = mumbai_city.find_all("td")[1].text
#city_rain = city_rain.replace("\n\n","")
#city_rain = float(city_rain)
mumbai_sub = table.find_all("tr")[11]
sub_rain = mumbai_sub.find_all("td")[1].text
#sub_rain = sub_rain.replace("\n\n","")
#sub_rain = float(sub_rain)
date
city_rain
sub_rain
