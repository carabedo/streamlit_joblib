# Clase 27: Flask, Streamlit, Heroku

La idea de la clase es mostrar 2 maneras de poner nuestro modelito o rutina de python online.

* en la practica 1 explicamos el modelito que usamos de excusa para aprender FLASK y STREAMLIT
* en la practica 2 creamos nuestras apps en flask 
* en la practica 3 accedemos a nuestra app de flask y motivamos el uso de streamlit

En practica 3 vemos el tipo de interaccion con usuarios que nos permite flask, hay que mirar esos codigos y en simultaneo vamos levantando esos servidores en la practica 2.

### 1 flask

la estructura mas basica de una app de flask:

```python
from flask import Flask
app = Flask('mi app')
@app.route('/',methods=['GET','POST])
def main():
    print('hola!')
app.run(host='127.0.0.1',  port=5000)
```
Debemos poner todo esto en un archivo.py y ejecutarlo desde la consola:

```bash
python archivo.py
``` 

### 2 streamlit
Las apps de streamlit, son mas simples, es un script de python normal y vamos insertando los widgets que necesitamos en el cuerpo del script. Aca una lista de los widgets disponibles https://docs.streamlit.io/api.html
Un ejemplo basico:

```python
import streamlit as st
st.write('hola!')
```
Lo guardamos en un archivo.py y para ejecutarlo:

```bash
streamlit run archivo.py
``` 


* bokeh_flask.py: archivo con nuestro ejemplo de implementacion de un servidor de FLASK que recibe requests GET
* bokeh_st.py: archivo con la implementacion del ejemplo anterior hecho en streamlit
* stream_ej.ppy: archivo con la app de stream que implementa todo el ejercicio plantedo en la practica 1
* en la carpeta templates hay un index.html, necesario para el ejmplo de bokeh en flask de la practica 2




### 3 Heroku [tutorial](https://github.com/carabedo/flask_streamlit/blob/master/Heroku.pdf): 

una vez que nuestras apps de streamlit funcionen como queremos, ya podemos subirlas. para crear la maquia virtual en heroku, tenemos que especificar la version de python y de las librerias presentes en nuestra app, esto lo hacemos en los archivos requirements y runtime. heroku tiene su propia aplicacion para interactuar con los archivos, yo prefiero que este sincronizado con mis repositorios en github, para esto primero nos creamos una cuenta en github, luego creamos un repositorio y ponemos los 5 archivos necesarios:

**nuestra app_st.py y cuatro archivos mas:**


```bash
app_st.py
requirements.txt
runtime.txt
Procfile
create_config.sh
``` 
revisen siempre los nombres de los archivos y los contenidos, si en creat_config.sh habla de un app.py y su app se llama app_st.py, tienen que cambiarlo.


ejemplos del contenido de estos archivos esta en:

https://github.com/carabedo/geopami

esta app esta funcionando en:

https://geopami.herokuapp.com/
