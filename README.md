# consultaBI
clasificador de tweets de la consulta popular 4 de Febrero 2017
# ESCUELA POLITECNICA NACIONAL
# INGENIERIA DE SISTEMAS
# INTELIGENCIA DE NEGOCIOS

# Integrantes:
* Carlos Gutierrez
* Andrea Villacis

# Tema:
Implementacion de un clasificador para saber si la consulta gano el SI o NO

# Objetivo
El objetivo de nuestro proyecto es investigar el funcionamiento de un clasificador de sentimientos donde se utilizará el algoritmo de redes neuronales orientado en lenguaje de programacion (Java) y para recolectar los tweets utilizaremos el motor de busqueda couchDB además para la clasificacion de los tweets utilizaremos Python.

# Herramientas
Python 2.7
Eclipse
CouchDB

# Fases del proyecto
1. Adquisicion de datos
2. Pre-procesamiento
3. Procesamiento
4. Analisis
5. Presentacion


1.	Adquisión de datos. - Para esta fase es necesario recolectar datos utilizando un cosechador de tweets entregado al inicio de este curso a través del aula virtual. En dicho cosechador, se establecieron las coordenadas necesarias para capturar tweets correspondientes a la ciudad de Quito Las herramientas utilizadas para esta fase corresponden a un script codificado en Python y una base de datos noSQL(CouchDb).

2.	Pre-procesamiento.- Será necesario filtrar los tweets correspondientes a las ciudades de Quito, Guayaquil y Cuenca, utilizando vistas en la base de datos o cualquier otra técnica que ustedes consideren conveniente. Además, será necesario filtrar tweets únicamente correspondientes al idioma español.


3.	Procesamiento. - Una vez que se tengan los tweets, será necesario procesar su campo “texto” para poder determinar la opinión pública respecto a la consulta popular. El procesamiento de texto de un tweet generalmente involucra la remoción de caracteres especiales, links, tags, etc. En este caso será necesario identificar y filtrar los tweets relacionados a la consulta popular.

4.	Análisis. - Es necesario realizar un análisis sobre el texto de cada tweet, para minar la opinión pública de las 3 ciudades. En este caso se deberá diseñar un clasificador en español que permita identificar la tendencia del voto por el sí o por el no en cada ciudad de tal forma que se logre una exactitud de clasificación alta. En este sentido será muy importante determinar las características necesarias (i.e vector de características) del data set de entrenamiento para lograr una alta exactitud de clasificación.

5.	Presentación. - Para esta fase se sugiere la utilización de herramientas con las cuales sea posible presentar gráficos, tablas, o elementos que permitan comprender fácilmente los resultados. Una sugerencia es utilizar gráficos para identificar los porcentajes para el SI y el NO en cada ciudad y mapas de calor para identificar las zonas, en cada ciudad en las que más se envían tweets respecto a la consulta. Para esto último será necesario utilizar el campo coordinates del tweet (siempre y cuando lo tengan activado) Cualquier otra forma de visualización será apreciada.


