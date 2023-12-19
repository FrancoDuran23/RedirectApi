# README.md

## Redirect API

Este proyecto en Django implementa un sistema de redirect de URLs con vistas basadas en clases para gestionar operaciones CRU. También incluye la vista personalizada 
GetUrlView que utiliza la caché para optimizar la búsqueda de URLs.

## Requisitos previos

Asegúrate de tener los siguientes requisitos previos instalados en tu sistema:

- Python 3.x: [Descargar Python](https://www.python.org/downloads/)
- Pip: [Instalación de Pip](https://pip.pypa.io/en/stable/installing/)
- Virtualenv (opcional pero recomendado): [Instalación de Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

## Configuración del entorno

1. Clona este repositorio en tu máquina local.

2. Abre una terminal y navega hasta la carpeta raíz del proyecto.

3. Crea un entorno virtual (opcional pero recomendado) ejecutando el siguiente comando:

    ```bash
    virtualenv venv
    ```

4. Activa el entorno virtual ejecutando el siguiente comando:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS y Linux:
     ```bash
     source venv/bin/activate
     ```

5. Instala las dependencias del proyecto ejecutando el siguiente comando:
    ```bash
    pip install -r requirements.txt
    ```

6. Configura las variables de entorno en un archivo `.env` en la raíz del proyecto. Puedes copiar el archivo `.env.example` y proporcionar los valores necesarios.
  
7. Instalación de Memcached 
  ```bash
  sudo apt-get update
  sudo apt-get install memcached
  ```
## Ejecución del proyecto

Una vez que hayas configurado el entorno, puedes ejecutar el proyecto localmente:

1. Inicia el servidor de desarrollo ejecutando el siguiente comando:
  ```
  python manage.py runserver
  ```
2. Accede a la API en tu navegador web en la siguiente dirección:
  ```
  http://localhost:8000/
  ```
Ahora deberías tener el proyecto de Django Rest Framework en funcionamiento en tu entorno local.

### Uso

#### Endpoints

- **Crear o Listar Redirects**: Endpoint para crear nuevas redirects o listar las existentes.

    - URL: `/redirect/`
    - Método: `GET` (listar redirects) / `POST` (crear redirect)
    - Campos requeridos (para `POST`): `key`, `url`, `active`

- **Recuperar, Actualizar Redirect**: Endpoint para recuperar o actualizar una redirect específica.

    - URL: `/redirect/<str:pk>/`
    - Método: `GET` (recuperar) / `PUT` (actualizar) 

- **Obtener URL por Key**: Endpoint para recuperar una URL basada en la key proporcionada. Verifica la caché primero y la actualiza si es necesario.

    - URL: `/get_url/<str:key>/`
    - Método: `GET`
    - Parámetro requerido: `key`
