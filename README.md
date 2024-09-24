# Tienda de Café IT

Este proyecto tiene fines educativos y pertenece a la comunidad de desarrolladores de Café IT - Sgo Del Estero

### Requisitos
* Tener instalado el interprete de Python
* Muchas ganas de aprender

### Pasos para tener el proyecto en tu compu

1. Bajar el repositorio
    ```bash
    git clone https://github.com/SebaSavino/tienda-cafe-it-sgo-django
    ```

2. Crear un entorno virtual dentro de la misma carpeta con el nombre "venv" para que sea ignorado (.gitignore) y no se suba a Github

    * Windows
    ```bash
    python -m venv venv
    ```

3. (IMPORTANTE) Activar el entorno

    * Windows
    ```bash
    .\venv\Scripts\activate
    ```

4. Instalar las dependencias en el entorno virtual

    ```bash
    pip install -r requirements.txt
    ```

5.  Pasamos los modelos a la base de datos (sqlite, no se compliquen)

    ```bash
    python .\manage.py migrate
    ```

6. Le damos corriente

    ```bash
    cd tienda
    python .\manage.py runserver
    ```