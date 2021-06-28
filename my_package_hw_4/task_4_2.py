import requests
import xml.etree.ElementTree as ET

# name_currency = input('Введите международное обозначение валюты большими буквами ')

def currency_rates(name_currency):
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    data_text = r.text
    data_root = ET.fromstring(data_text)
    if name_currency == 'USD':
        print(f'На сегоднящний день Доллар равен {data_root[10][4].text} рублей')
    elif name_currency == 'EUR':
        print(f'На сегоднящний день Доллар равен {data_root[11][4].text} рублей')
    else:
        print('Я так не умею')

currency_rates('USD')
currency_rates('EUR')