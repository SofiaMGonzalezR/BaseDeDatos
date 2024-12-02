# Instrucciones de Dependencias del Proyecto

Este proyecto utiliza un conjunto de dependencias que se gestionan mediante `pip`. A continuación, se detallan las instrucciones para instalar y gestionar las dependencias necesarias para ejecutar este proyecto.

## Requisitos previos

Asegúrate de tener instalada una versión reciente de **Python** (se recomienda Python 3.6 o superior). Además, asegúrate de tener **pip** actualizado. Si no tienes pip, puedes instalarlo ejecutando:

```bash
python -m ensurepip --upgrade
```

## 1. Configuración del Entorno Virtual

Para evitar conflictos con otras dependencias en tu sistema, es recomendable crear un entorno virtual. Para ello, sigue estos pasos:

### a) Crear un entorno virtual

```
python -m venv venv
```

### b) Activar el entorno virtual

#### Windows

```
.\venv\Scripts\activate
```
#### macOS o Linux:

```
source venv/bin/activate
```

## 2. Instalación de las Dependencias
Una vez tengas el entorno virtual activo, instala las dependencias necesarias para este proyecto ejecutando:

```
pip install -r requirements.txt
```
Esto instalará todas las dependencias definidas en el archivo `requirements.txt`.

## 3. Dependencias del Proyecto
Las dependencias incluidas en el archivo `requirements.txt` son las siguientes:

- `markdown-it-py: 3.0.0`: Biblioteca para procesar Markdown en Python.
- `mdurl: 0.1.2`: Utilizado por markdown-it-py para manejar URLs en Markdown.
- `mysql-connector-python: 9.1.0`: Conector de MySQL para Python, utilizado para interactuar con bases de datos MySQL.
- `Pygments: 2.18.0`: Biblioteca para el resaltado de sintaxis, utilizada para mostrar código de manera legible.
- `python-dotenv: 1.0.1`: Carga variables de entorno desde archivos .env.
- `rich: 13.9.4`: Biblioteca para crear interfaces de usuario en la terminal con colores y estilos avanzados.
- `tabulate: 0.9.0`: Utilizada para mostrar tablas de manera legible en la terminal.

## 4. Uso del Proyecto

Una vez que hayas instalado las dependencias, puedes comenzar a trabajar con el proyecto según los requerimientos definidos en tu código. Asegúrate de configurar cualquier archivo de configuración, como `.env`, para que las credenciales y las configuraciones sean correctas para tu entorno.
