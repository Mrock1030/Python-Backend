# Proyecto Backend: API REST de Gestión de Tareas con Python

## Descripción del Proyecto
Una API REST completa para gestionar tareas (To-Do List) construida con Flask y SQLite. Incluye autenticación, validación de datos y documentación.

## Tecnologías Utilizadas
- Python 3.8+
- Flask (Framework web)
- SQLite (Base de datos)
- JWT (Autenticación)
- Flask-CORS (Manejo de CORS)

## Paso 1: Configuración Inicial

### 1.1 Crear estructura del proyecto
```bash
mkdir task-api
cd task-api
```

### 1.2 Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 1.3 Instalar dependencias
```bash
pip install flask flask-cors pyjwt python-dotenv
pip freeze > requirements.txt
```

### 1.4 Estructura de carpetas
```
task-api/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── auth.py
├── database/
│   └── database.db (se genera automáticamente)
├── .env
├── .gitignore
├── requirements.txt
├── config.py
└── run.py
```

## Paso 2: Configuración Base

### 2.1 Crear archivo `.env`
```env
SECRET_KEY=tu_clave_secreta_super_segura_aqui
DATABASE_PATH=database/database.db
```

### 2.2 Crear archivo `config.py`
```python
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DATABASE_PATH = os.getenv('DATABASE_PATH', 'database/database.db')
```

### 2.3 Crear archivo `.gitignore`
```
venv/
*.pyc
__pycache__/
.env
database/*.db
.DS_Store
```

## Paso 3: Crear Modelos de Base de Datos

### 3.1 Archivo `app/models.py`
```python
import sqlite3
from datetime import datetime
import os

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.init_db()
    
    def get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def init_db(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Tabla de usuarios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Tabla de tareas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                completed BOOLEAN DEFAULT 0,
                user_id INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        conn.commit()
        conn.close()
```

## Paso 4: Implementar Autenticación

### 4.1 Archivo `app/auth.py`
```python
import jwt
import hashlib
from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify
from config import Config

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token:
            return jsonify({'message': 'Token faltante'}), 401
        
        try:
            if token.startswith('Bearer '):
                token = token.split(' ')[1]
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
            current_user_id = data['user_id']
        except:
            return jsonify({'message': 'Token inválido'}), 401
        
        return f(current_user_id, *args, **kwargs)
    
    return decorated
```

## Paso 5: Crear Rutas de la API

### 5.1 Archivo `app/routes.py`
```python
from flask import Blueprint, request, jsonify
from app.models import Database
from app.auth import hash_password, generate_token, token_required
from config import Config

api = Blueprint('api', __name__)
db = Database(Config.DATABASE_PATH)

# Registro de usuario
@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'message': 'Usuario y contraseña requeridos'}), 400
    
    conn = db.get_connection()
    cursor = conn.cursor()
    
    try:
        hashed_password = hash_password(password)
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                      (username, hashed_password))
        conn.commit()
        return jsonify({'message': 'Usuario creado exitosamente'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'message': 'El usuario ya existe'}), 400
    finally:
        conn.close()

# Login
@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    conn = db.get_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, password FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    
    if user and user[1] == hash_password(password):
        token = generate_token(user[0])
        return jsonify({'token': token}), 200
    
    return jsonify({'message': 'Credenciales inválidas'}), 401

# Obtener todas las tareas del usuario
@api.route('/tasks', methods=['GET'])
@token_required
def get_tasks(current_user_id):
    conn = db.get_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM tasks WHERE user_id = ?', (current_user_id,))
    tasks = cursor.fetchall()
    conn.close()
    
    task_list = []
    for task in tasks:
        task_list.append({
            'id': task[0],
            'title': task[1],
            'description': task[2],
            'completed': bool(task[3]),
            'created_at': task[5]
        })
    
    return jsonify({'tasks': task_list}), 200

# Crear nueva tarea
@api.route('/tasks', methods=['POST'])
@token_required
def create_task(current_user_id):
    data = request.get_json()
    title = data.get('title')
    description = data.get('description', '')
    
    if not title:
        return jsonify({'message': 'El título es requerido'}), 400
    
    conn = db.get_connection()
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO tasks (title, description, user_id) VALUES (?, ?, ?)',
                  (title, description, current_user_id))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    
    return jsonify({'message': 'Tarea creada', 'task_id': task_id}), 201

# Actualizar tarea
@api.route('/tasks/<int:task_id>', methods=['PUT'])
@token_required
def update_task(current_user_id, task_id):
    data = request.get_json()
    
    conn = db.get_connection()
    cursor = conn.cursor()
    
    # Verificar que la tarea pertenece al usuario
    cursor.execute('SELECT id FROM tasks WHERE id = ? AND user_id = ?',
                  (task_id, current_user_id))
    if not cursor.fetchone():
        conn.close()
        return jsonify({'message': 'Tarea no encontrada'}), 404
    
    title = data.get('title')
    description = data.get('description')
    completed = data.get('completed')
    
    updates = []
    values = []
    
    if title is not None:
        updates.append('title = ?')
        values.append(title)
    if description is not None:
        updates.append('description = ?')
        values.append(description)
    if completed is not None:
        updates.append('completed = ?')
        values.append(int(completed))
    
    if updates:
        query = f'UPDATE tasks SET {", ".join(updates)} WHERE id = ?'
        values.append(task_id)
        cursor.execute(query, values)
        conn.commit()
    
    conn.close()
    return jsonify({'message': 'Tarea actualizada'}), 200

# Eliminar tarea
@api.route('/tasks/<int:task_id>', methods=['DELETE'])
@token_required
def delete_task(current_user_id, task_id):
    conn = db.get_connection()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM tasks WHERE id = ? AND user_id = ?',
                  (task_id, current_user_id))
    conn.commit()
    
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({'message': 'Tarea no encontrada'}), 404
    
    conn.close()
    return jsonify({'message': 'Tarea eliminada'}), 200
```

## Paso 6: Inicializar la Aplicación

### 6.1 Archivo `app/__init__.py`
```python
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    CORS(app)
    
    from app.routes import api
    app.register_blueprint(api, url_prefix='/api')
    
    return app
```

### 6.2 Archivo `run.py`
```python
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

## Paso 7: Ejecutar el Proyecto

```bash
python run.py
```

La API estará disponible en `http://localhost:5000`

## Paso 8: Probar los Endpoints

### Usando curl o Postman:

**Registro:**
```bash
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{"username":"usuario1","password":"password123"}'
```

**Login:**
```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"usuario1","password":"password123"}'
```

**Crear tarea (con token):**
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer TU_TOKEN_AQUI" \
  -d '{"title":"Mi primera tarea","description":"Descripción de la tarea"}'
```

## Paso 9: Crear README.md para GitHub

```markdown
# Task API - Sistema de Gestión de Tareas

API REST desarrollada con Python y Flask para gestionar tareas con autenticación JWT.

## Características
- Autenticación con JWT
- CRUD completo de tareas
- Base de datos SQLite
- Validación de datos
- Relación usuario-tareas

## Instalación
1. Clonar el repositorio
2. Crear entorno virtual: `python -m venv venv`
3. Activar entorno: `source venv/bin/activate`
4. Instalar dependencias: `pip install -r requirements.txt`
5. Crear archivo .env con SECRET_KEY
6. Ejecutar: `python run.py`

## Endpoints
- POST /api/register - Registro de usuario
- POST /api/login - Autenticación
- GET /api/tasks - Obtener tareas
- POST /api/tasks - Crear tarea
- PUT /api/tasks/:id - Actualizar tarea
- DELETE /api/tasks/:id - Eliminar tarea

## Tecnologías
- Python 3.8+
- Flask
- SQLite
- JWT
```

## Paso 10: Subir a GitHub

```bash
git init
git add .
git commit -m "Initial commit: Task API backend"
git branch -M main
git remote add origin https://github.com/tu-usuario/task-api.git
git push -u origin main
```

## Mejoras Futuras
- Agregar paginación a las tareas
- Implementar filtros por estado (completadas/pendientes)
- Agregar tests unitarios
- Dockerizar la aplicación
- Implementar rate limiting
- Agregar documentación con Swagger

---

Este proyecto demuestra conocimientos en desarrollo backend, manejo de bases de datos, autenticación, y buenas prácticas de programación.