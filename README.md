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

* **Número de recomendaciones personalizadas**

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
│   ├── recommendations.py
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

## Usando los instaladores oficiales

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Usando PyPI o pipx

**Con pip:**

```bash
pip install uv
```

**Con pipx:**

```bash
pipx install uv
```

> Si instalaste `uv` mediante los instaladores oficiales, puedes actualizarlo a la última versión con:
>
> ```bash
> uv self update
> ```

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
uv run sistemas-recomendacion -f data/ejemplo.txt -m pearson -k 2 -t simple -r 5
```

O ejecutando directamente el script principal:

```bash
uv run src/main.py -f data/ejemplo.txt -m pearson -k 2 -t simple -r 5
```

---

## 🧩 Opciones de ejecución

```bash
usage: main.py [-h] -f FILE [-m {pearson,cosine,euclidean}] [-k NEIGHBORS] [-t {simple,mean_difference} [-r NUM_RECOMMENDATIONS]]
```

* `-h` o `--help`: Muestra la ayuda del programa
* `-f FILE` o `--file FILE`: Fichero que contiene la matriz de utilidad
* `-m` o `--metric`: Métrica a usar (por defecto: `pearson`)
  Opciones: `pearson`, `cosine`, `euclidean`
* `-k NEIGHBORS` o `--neighbors NEIGHBORS`: Número de vecinos a considerar (por defecto: 2)
* `-t {simple, mean_difference}` o `--type {simple, mean_difference}`: Tipo de predicción (por defecto: `simple`)
* `-r NUM_RECOMMENDATIONS` o `--recommendations NUM_RECOMMENDATIONS`: Número de ítems recomendados (por defecto: 3)

---

## 📄 Breve descripción de los scripts

* `main.py`: Ejecuta la generación de la matriz de utilidad y la matriz de similitudes
* `cli.py`: Interfaz de línea de comandos
* `fill.py`: Funciones para completar la matriz de utilidad
* `metrics.py`: Cálculo de similitudes entre usuarios
* `predictions.py`: Predicción de valoraciones
* `recommendations.py`: Funciones de recomendación de items
* `utils.py`: Funciones auxiliares
