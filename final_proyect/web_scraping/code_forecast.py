from bs4 import BeautifulSoup
import requests

# Ingresar al pronostico de la pagina web WEATHER
url = 'https://weather.com/es-PE/tiempo/10dias/l/56ae2f14da2603f93bf9a43126ca1dba616814154b6f2d2f87c2ef6bfcb080b4#detailIndex5'
page = requests.get(url)

# Obtener contenido de la pagina web
soup = BeautifulSoup(page.content, 'html.parser')

# Seleccionar predicciones
dias = [x.text for x in soup.find_all('h2', class_ = 'DetailsSummary--daypartName--1Mebr')]
max_temp = [x.text for x in soup.find_all('span', class_ = 'DetailsSummary--highTempValue--3x6cL')]
min_temp = [x.text for x in soup.find_all('span', class_ = 'DetailsSummary--lowTempValue--1DlJK')]
estado = [x.text for x in soup.find_all('span', class_ = 'DetailsSummary--extendedData--aaFeV')]
viento = [x.text for x in soup.find_all('span', class_ = 'Wind--windWrapper--1Va1P undefined')]

def send_data_forecast():
    data = [dias, max_temp, min_temp, estado, viento]
    return data
