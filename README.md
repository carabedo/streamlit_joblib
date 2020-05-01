# Clase 27: Flask, Streamlit, Heroku

La idea de la clase es mostrar 2 maneras de poner nuestro modelito o rutina de python online.

* en la practica 1 explicamos el modelito que usamos de excusa para aprender FLASK y STREAMLIT
* en la practica 2 creamos nuestras apps en flask 
* en la practica 3 accedemos a nuestra app de flask y motivamos el uso de streamlit

En practica 3 vemos el tipo de interaccion con usuarios que nos permite flask, hay que mirar esos codigos y en simultaneo vamos levantando esos servidores en la practica 2.

* bokeh_flask.py: archivo con nuestro ejemplo de implementacion de un servidor de FLASK que recibe requests GET
* bokeh_st.py: archivo con nuestro ejemplo de implementacion del ejemplo de bokeh hecho en streamlit
* stream_ej.ppy: archivo con la app de stream que implementa todo el ejercicio plantedo en la practica 1

* en la carpeta templates hay un index.html, necesario para el ejmplo de bokeh en flask de la practica 2


### podemos correr los servidores desde las consolas
+ streamlit: 

```bash
streamlit run app_st.py
``` 

+ flask: 

```bash
python app_flask.py
``` 
### una vez que nuestras apps de streamlit funcionen como queremos, ya podemos subirlas a heroku

para necesitamos nuestra app_st.py y cuatro archivos mas, ejemplos de esto estan en la carpeta heroku

```bash
requirements.txt
runtime.txt
Procfile
make_install.c
``` 
