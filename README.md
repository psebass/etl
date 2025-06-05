[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](#)



# Simple ETL

Utilidad base muy simple, desarrollada en Python con el framework Flask para limpiar archivos Excel.

## Funcionamiento
Desde un frontend web se puede seleccionar uno o varios archivos .xlsx o .csv para que el backend de la aplicación haga una limpieza simple. Se puede adaptar a gusto y necesidad.

## Limpieza
* Se quitan las columnas vacías.
* Se quitan espacios en los nombres de las cabeceras.
* Se reemplazan acentos en los nombres de las cabeceras.
* Convierte a minúsculas los nombres de las cabeceras.
* Elimina filas duplicadas.
* Rellena nulos con un guión.  

Toda esta limpieza es totalmente personalizable de acuerdo a la necesidad de limpieza que se quiera llevar a cabo.

## Autor

- [@psebass](https://www.github.com/psebass)

## Futuro
Seleccionar los procesos de limpieza desde el frontend para adaptar la transformación a cada procesamiento.