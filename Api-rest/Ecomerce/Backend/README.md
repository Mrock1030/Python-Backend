# E-commerce REST API

Este es el backend de una API REST para una aplicación de comercio electrónico, construida con Python y Flask. Proporciona endpoints para gestionar usuarios, productos y compras, con control de acceso basado en roles.

## Características

-   Registro e inicio de sesión de usuarios (basado en JWT).
-   Autorización basada en roles (`admin`, `cliente`).
-   Operaciones CRUD para clientes (usuarios con rol 'cliente').
-   Listado y paginación de todos los clientes (solo para administradores).
-   Envío de correo electrónico de bienvenida al registrarse.
-   Validaciones de datos en la creación de usuarios.

## Tecnologías Utilizadas

-   Python
-   Flask
-   Flask-RESTful
-   Flask-SQLAlchemy
-   Flask-JWT-Extended
-   Flask-Mail
-   Werkzeug

## Instalación y Puesta en Marcha

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

1.  **Clona el repositorio:**
    ```bash
    git clone <URL-DEL-REPOSITORIO>
    cd Backen-Ecomerce/Api-rest/Ecomerce/Backend
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    # Para Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    (Asegúrate de tener un archivo `requirements.txt` con todas las librerías necesarias).
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configura las variables de entorno:**
    Crea un archivo `.env` en el directorio raíz (`Backend`) a partir del archivo `.env.example`.

    ```bash
    cp .env.example .env
    ```

    Luego, edita el archivo `.env` con tu configuración específica (email, contraseñas, claves secretas).

5.  **Ejecuta la aplicación:**
    El comando `python app.py` inicializará la base de datos y ejecutará la aplicación.
    ```bash
    python app.py
    ```
    La API estará disponible en `http://127.0.0.1:5000` (o el puerto que hayas configurado en el archivo `.env`).

## Estructura del Proyecto

```
Backend/
├── app.py              # Punto de entrada de la aplicación
├── main/
│   ├── __init__.py     # Inicialización de la app Flask y extensiones
│   ├── auth/           # Módulo de autenticación y autorización
│   ├── help/           # Clases de ayuda y utilidades
│   ├── mail/           # Lógica para el envío de correos
│   ├── models/         # Modelos de la base de datos (SQLAlchemy)
│   ├── resources/      # Recursos de la API (Flask-RESTful)
│   └── templates/      # Plantillas de correo
├── .env                # Variables de entorno (local, no versionado)
├── .env.example        # Ejemplo de variables de entorno
└── requirements.txt    # Dependencias de Python
```

## Endpoints de la API

### Autenticación (`/auth`)

-   `POST /auth/register`
    -   Registra un nuevo usuario con el rol de `cliente`.
    -   **Body (raw, JSON):**
        ```json
        {
            "nombre": "Juan",
            "apellido": "Perez",
            "email": "juan.perez@example.com",
            "password": "una_contraseña_segura",
            "telefono": 1122334455
        }
        ```

-   `POST /auth/login`
    -   Autentica a un usuario y devuelve un token de acceso JWT.
    -   **Body (raw, JSON):**
        ```json
        {
            "email": "juan.perez@example.com",
            "password": "una_contraseña_segura"
        }
        ```

### Clientes (`/cliente`, `/clientes`)

-   `GET /clientes`: **Rol requerido:** `admin`. Devuelve una lista paginada de todos los clientes.
-   `POST /clientes`: **Rol requerido:** `admin`. Crea un nuevo cliente.
-   `GET /cliente/<id>`: **Rol requerido:** `admin` o el propio `cliente`. Devuelve los detalles de un cliente.
-   `PUT /cliente/<id>`: **Rol requerido:** `admin` o el propio `cliente`. Actualiza los datos de un cliente.
-   `DELETE /cliente/<id>`: **Rol requerido:** `admin` o el propio `cliente`. Elimina un cliente.