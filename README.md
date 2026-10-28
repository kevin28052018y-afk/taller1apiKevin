# 🎓 SENA - Plataforma de Gestión de Aprendices

> **Backend Engine:** API REST de alto rendimiento construida sobre **FastAPI** y **MongoDB Atlas**, complementada con una interfaz interactiva de terminal (**CLI**) para la gestión operativa de los registros del SENA.

---

### 🌐 Ecosistema en la Nube
* **Servicio REST en Producción:** [https://onrender.com](https://onrender.com)
* **Especificación e Interfaz Swagger:** [https://onrender.comdocs](https://onrender.comdocs)

---

## 📝 Ficha Técnica del Proyecto

### Información del Autor
* **Desarrollador:** Kevin Alejandro Osorio Parra
* **Código de Ficha:** 3494620
* **Núcleos de Competencia:**
  * Elaboración de la propuesta técnica para la solución de software.
  * Implantación del software.

### Enfoque Arquitectónico
Este proyecto formativo implementa una arquitectura de software desacoplada en capas sobre Python. Garantiza la integridad de la información mediante validaciones estrictas en el lado del servidor con Pydantic, almacenamiento persistente no relacional en la nube (MongoDB Atlas) y un cliente de consola síncrono/asíncrono potenciado por HTTPX para consumir el servicio de forma ágil.

---

## 📊 Estructura del Modelo de Datos

El sistema modela y audita las siguientes propiedades por cada aprendiz:

| Atributo | Tipo de Dato / Validación | Descripción |
| :--- | :--- | :--- |
| **Documento** | Alfanumérico / Único | Identificación oficial del estudiante. |
| **Nombres** | Cadena de texto | Nombres de pila del usuario. |
| **Apellidos** | Cadena de texto | Apellidos familiares del usuario. |
| **Correo** | Estructura EmailStr | Dirección electrónica institucional o personal validada. |
| **Edad** | Entero positivo | Edad cronológica registrada. |
| **Programa** | Cadena de texto | Denominación del programa de formación técnica/tecnológica. |
| **Ficha** | Alfanumérico | Código identificador del grupo de estudio. |

---

## ⚡ Stack Tecnológico

| Componente | Tecnología | Rol en el Sistema |
| :--- | :--- | :--- |
| **Core** | Python 3.10+ | Lenguaje base de la solución. |
| **Web Framework** | FastAPI | Enrutamiento moderno, asincronía y documentación auto-generada. |
| **ASGI Server** | Uvicorn | Motor de servicios para el despliegue local de la API. |
| **Persistence** | MongoDB Atlas & PyMongo | Base de datos NoSQL Cloud y driver oficial de comunicación. |
| **Validation Layer** | Pydantic | Tipado estricto y parsing de esquemas JSON. |
| **HTTP Client** | HTTPX | Consumo de endpoints asíncronos desde el entorno CLI. |
| **Configuration** | Python-dotenv | Aislamiento seguro de variables de entorno y secretos. |
| **Cloud Hosting** | Render | Infraestructura PaaS para el despliegue del backend. |

---

## 📂 Organización del Repositorio

El código fuente sigue un patrón de responsabilidades separadas dentro del directorio principal `fastapi/`:

```text
       [ src/ ]
          ├── main.py        <-- Enrutador principal y configuración de la API REST
          ├── controllers.py <-- Lógica del negocio y operaciones CRUD (PyMongo)
          ├── database.py    <-- Inicialización del cliente y enlace a MongoDB Cloud
          ├── model.py       <-- Definición de esquemas de datos (Pydantic Models)
          │
          ├── [ views/ ]     
          │     └── view.py  <-- Interfaz de Línea de Comandos (CLI) vía HTTPX
          │
          └── [ templates/ ] <-- Formateadores y maquetación de salida en consola
       
       [ data/ ]             <-- Repositorio local de almacenamiento temporal
       [ test/ ]             
          └── test_main.py   <-- Suite de pruebas unitarias y de integración
```

---

## 📡 Matriz de Endpoints (API Gateway)

| Operación | Ruta del Recurso | Objetivo del Endpoint |
| :--- | :--- | :--- |
| `GET` | `/` | Monitor de estado de la aplicación (*Health Check*). |
| `POST` | `/trainees` | Inserción y validación de un nuevo expediente de aprendiz. |
| `GET` | `/trainees` | Extracción del catálogo completo de alumnos registrados. |
| `GET` | `/trainees/{trainee_id}` | Localización de un aprendiz específico mediante su `_id` de MongoDB. |
| `PUT` | `/trainees/{trainee_id}` | Actualización parcial o total de las propiedades del registro. |
| `DELETE` | `/trainees/{trainee_id}` | Purga absoluta del registro en el cluster de datos. |

---

## 💻 Guía de Despliegue Local

### 1. Clonación del Entorno
```bash
git clone https://github.com
cd fastapi
```

### 2. Aislamiento del Entorno Virtual

* **Sistemas Unix (Linux / macOS):**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* **Entornos Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### 3. Aprovisionamiento de Dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Setup de Variables de Entorno
Duplique la plantilla base del archivo de configuración:
```bash
cp .env.example .env
```
Abra el archivo `.env` recién creado e inyecte sus credenciales operativas:
```env
MONGO_URL=mongodb+srv://<usuario>:<password>@<cluster>.mongodb.net/
BASE_URL=https://onrender.com
```
> 💡 *Nota Técnica:* Para redirigir el consumo del CLI (`view.py`) hacia el entorno de desarrollo local en lugar del servidor de Render, reemplace el valor de `BASE_URL` por `http://127.0.0.1:8000`.

### 5. Lanzamiento del Servidor API
```bash
uvicorn src.main:app --reload
```
* Acceso a la API local: `http://127.0.0.1:8000`
* Acceso a la documentación interactiva: `http://127.0.0`

### 6. Ejecución del Entorno de Consola (CLI)
Abra una ventana de terminal adicional, asegúrese de tener el entorno virtual activo e invoque la interfaz visual:
```bash
python src/views/view.py
```
