from bs4 import BeautifulSoup
import requests

# Ingresar a la pagina web de WEATHER
url = 'https://weather.com/es-PE/tiempo/hoy/l/PEXX0011:1:PE?Goto=Redirected'
page = requests.get(url)

# Obtener contenido de la pagina web
soup = BeautifulSoup(page.content, 'html.parser')

# Eliminar svg
for s in soup.select('svg'):
    s.extract()

# Seleccionar informacion del dia
temp = soup.find('span', class_ = 'TodayDetailsCard--feelsLikeTempValue--2aogo').text
estado = soup.find('div', class_ = 'CurrentConditions--phraseValue--2xXSr').text
detalles = [x.text for x in soup.find_all('div', class_ = 'WeatherDetailsListItem--wxData--23DP5')]

def send_data_actual():
    data = [temp, estado] + detalles
    return data
