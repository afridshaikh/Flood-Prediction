import csv
import requests
import string
from bs4 import BeautifulSoup
r = requests.get("http://www.imdmumbai.gov.in/scripts/detail.asp?releaseid=E2015RF4")
soup = BeautifulSoup(r.content)

