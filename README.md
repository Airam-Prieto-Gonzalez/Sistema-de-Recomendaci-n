# Sistema-de-Recomendación

Este programa es una implementación de un sistema de recomendación siguiendo el método de filtrado colaborativo,
teniendo como entrada un fichero con la matriz de utilidad.

El programa cuenta con las siguientes opciones:
* La métrica utilizada:
  - Correlación de Pearson
  - Distancia coseno
  - Distancia Euclídea
* El número de vecinos
* El tipo de predicción:
  - Predicción simple
  - Diferencia con la 
  
## Instalación y despliegue

Clonamos el repositorio, cambiamos al directorio, creamos un entorno virtual e instalamos las dependencias
```bash
git clone <>
cd Sistema-de-Recomendaci-on
python3 -m venv .venv
source .venv/bin/activate
pip install -r requeriments.txt
```

Y aquí tenemos un ejemplo de ejecución del programa
```bash
python3 src/main.py -f data/ejemplo.txt -m pearson -k 2 -t simple
```

## Opciones de ejecución

Aquí tenemos los parametros y argumentos posibles del programa
```bash
usage: main.py [-h] -f FILE [-m {pearson}] [-k NEIGHBORS] [-t {simple,mean_difference}]
```
* `-h` o `--help`: Muestra la ayuda del programa
* `-f FILE` o `--file FILE`: Fichero que contiene la matriz de utilidad
* `-m` o `--metric`: Opción para seleccionar la metrica a usar. (Por defecto: pearso)
<br>Opciones:
  - pearson
  - cosine
  - euclidean

* `-k NEIGHBORS` o `--neighbors NEIGHBORS`: Numero de vecinos a considerar. (Por defecto 2)
* `-t {simple, mean_difference}` o `--type {simple, mean_difference}`: Tipo de predicción. (Por defecto: simple)