import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/'
#obtengo la pagina a analizar
html_doc = requests.get(url)
#print(html_doc.text)
#parsear la pagina web
soup = BeautifulSoup(html_doc.text, 'html.parser')


titulo_datos = soup.h1.string
print(titulo_datos)

tabla = soup.find('table')

#obtener las filas de la tabla
filas = tabla.find_all('tr')
cedula = []
nombres = []
apellido = []
sexo = []
emails = []
carrera = []
vigencia = []

#iterar sobre las filas e imprimir los datos
for fila in filas:
    # obtener las celdas de la fila
    celdas = fila.find_all('td')
    if len(celdas)>0:
        cedula.append(celdas[1].string)
        apellido.append(celdas[2].string)
        nombres.append(celdas[3].string)
        sexo.append(celdas[4].string)
        emails.append(celdas[5].string)
        carrera.append(celdas[6].string)
        vigencia.append(celdas[7].string)

print(apellido)
print(nombres)
print(emails)

df = pd.DataFrame({ 'Nombres': nombres, 'Apellidos' : apellido,'Sexo' : sexo, 'Emails' : emails,'Carrera' : carrera, 'Vigencia' : vigencia })
df.to_csv('estudiantes.csv', index=False, encoding='utf-8')

