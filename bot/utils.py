import requests
from bs4 import BeautifulSoup

API_URL = "https://www.cbr.ru/scripts/XML_daily.asp"


def get_usd_to_rub_rate():
    response = requests.get(API_URL)
    soup = BeautifulSoup(response.content, "xml")
    print(soup)
    usd_value = soup.find("Valute", ID="R01235").Value.text
    return usd_value.replace(",", ".")
