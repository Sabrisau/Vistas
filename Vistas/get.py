import requests

url = 'http://localhost:8000/pages/saludo/'

params = {'nombre' : 'Sabri'}
response = requests.get(url,params=params)

if response.status_code == 200:
    print("Respuesta",response.text)
else: 
    print("Error en la solicitus", response.status_code)