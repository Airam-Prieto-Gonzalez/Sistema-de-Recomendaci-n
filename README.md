# Sistema de Recomendación

Este programa es una implementación de un sistema de recomendación siguiendo el método de **filtrado colaborativo**, teniendo como entrada un fichero con la **matriz de utilidad**.

El programa cuenta con las siguientes opciones:

* **Métrica utilizada**:

  * Correlación de Pearson
  * Distancia coseno
  * Distancia Euclídea
* **Número de vecinos**
* **Tipo de predicción**:

  * Predicción simple
  * Diferencia con la media (`mean_difference`)

---

## 📁 Estructura del proyecto

```
.
├── data/                  # Archivos de datos de ejemplo
├── docs/                  # Documentación y slides
├── pyproject.toml         # Configuración del proyecto y dependencias
├── README.md
├── src/                   # Código fuente
│   ├── main.py            # Punto de entrada principal
│   ├── cli.py
│   ├── fill.py
│   ├── metrics.py
│   ├── predictions.py
│   ├── utils.py
│   └── ...
└── uv.lock                # Archivo de lock de uv
```

---

## 🛠 Requisitos previos

* Python **3.12+**
* Git (opcional, para clonar el repositorio)
* Conexión a Internet para instalar dependencias

---

## ⚡ Instalación y despliegue con uv

1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd Sistema-de-Recomendacion
```

2. Instalar **uv** si no está instalado:

```bash
python3 -m pip install --user uv
uv --version
```

3. Sincronizar dependencias y crear el entorno virtual:

```bash
uv sync
uv sync --group dev   # opcional, instala herramientas de desarrollo como ruff
```

> Esto creará un entorno virtual `.venv` e instalará todas las dependencias definidas en `pyproject.toml`.

---

## ▶️ Ejemplo de ejecución

Usando el entrypoint definido en `pyproject.toml`:

```bash
uv run sistemas-recomendacion -f data/ejemplo.txt -m pearson -k 2 -t simple
```

O ejecutando directamente el script principal:

```bash
uv run src/main.py -f data/ejemplo.txt -m pearson -k 2 -t simple
```

---

## 🧩 Opciones de ejecución

```bash
usage: main.py [-h] -f FILE [-m {pearson,cosine,euclidean}] [-k NEIGHBORS] [-t {simple,mean_difference}]
```

* `-h` o `--help`: Muestra la ayuda del programa
* `-f FILE` o `--file FILE`: Fichero que contiene la matriz de utilidad
* `-m` o `--metric`: Métrica a usar (por defecto: `pearson`)
  Opciones: `pearson`, `cosine`, `euclidean`
* `-k NEIGHBORS` o `--neighbors NEIGHBORS`: Número de vecinos a considerar (por defecto: 2)
* `-t {simple, mean_difference}` o `--type {simple, mean_difference}`: Tipo de predicción (por defecto: `simple`)

---

## 📄 Breve descripción de los scripts

* `main.py`: Ejecuta la generación de la matriz de utilidad y la matriz de similitudes
* `cli.py`: Interfaz de línea de comandos
* `fill.py`: Funciones para completar la matriz de utilidad
* `metrics.py`: Cálculo de similitudes entre usuarios
* `predictions.py`: Predicción de valoraciones
* `utils.py`: Funciones auxiliares
