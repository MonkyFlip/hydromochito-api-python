
# Hydromochito API

## Descripción

La **Hydromochito API** es una aplicación desarrollada con **FastAPI**, diseñada para gestionar usuarios y datos IoT provenientes de sensores. Este proyecto utiliza una base de datos RDS alojada en **AWS** para almacenar la información y está preparado para integrarse con aplicaciones frontend creadas con **React** y **Expo**.



## Funcionalidades

- **Usuarios**:

  - Crear usuarios.
  - Consultar usuarios específicos.
  - Actualizar usuarios.
  - Eliminar usuarios.
  - Login con autenticación y encriptación segura de contraseñas utilizando bcrypt.

- **Registros IoT**:
  - Crear registros IoT.
  - Consultar registros específicos.
  - Consultar todos los registros en formato JSON.
  - Actualizar registros.
  - Eliminar registros.



## Requisitos

Antes de ejecutar la API, asegúrate de tener:

- Python 3.8 o superior.
- Acceso a tu base de datos RDS en AWS.
- Las dependencias especificadas en el archivo `requirements.txt`.



## Instalación

1. **Clona el repositorio**:

   git clone [https://tu-repositorio.git](https://github.com/MonkyFlip/hydromochito-api-python.git)
   cd hydromochito-api-python

2. **Configura un entorno virtual**:

   python -m venv venv
   source venv/bin/activate # En macOS/Linux
   venv\Scripts\activate # En Windows

3. **Instala las dependencias**:

   pip install -r requirements.txt

4. **Configura las credenciales**:
   - Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:
     plaintext
     DATABASE_URL=credenciales de la rds
     JWT_SECRET=secreto


## Uso

1. **Ejecuta la API**:

   uvicorn app.main:app --reload

2. **Accede a la documentación interactiva**:
   - Utiliza la interfaz Swagger para probar los endpoints.



## Endpoints

### Usuarios

| Método | Ruta             | Descripción                |
| ------ | ---------------- | -------------------------- |
| POST   | `/usuarios/`     | Crear un nuevo usuario.    |
| GET    | `/usuarios/{id}` | Obtener un usuario por ID. |
| PUT    | `/usuarios/{id}` | Actualizar un usuario.     |
| DELETE | `/usuarios/{id}` | Eliminar un usuario.       |

### Registros IoT

| Método | Ruta              | Descripción                    |
| ------ | ----------------- | ------------------------------ |
| POST   | `/registros/`     | Crear un nuevo registro IoT.   |
| GET    | `/registros/{id}` | Obtener un registro por ID.    |
| GET    | `/registros/all`  | Consultar todos los registros. |
| PUT    | `/registros/{id}` | Actualizar un registro IoT.    |
| DELETE | `/registros/{id}` | Eliminar un registro IoT.      |


## Tecnologías utilizadas

- **FastAPI**: Framework para desarrollar APIs rápidas y escalables.
- **SQLAlchemy**: ORM para interactuar con la base de datos RDS.
- **bcrypt**: Encriptación segura de contraseñas.
- **AWS RDS**: Base de datos PostgreSQL alojada en la nube.


## Autenticación

La API utiliza JWT para autenticar a los usuarios. Asegúrate de proporcionar el token en las solicitudes protegidas usando el encabezado `Authorization: Bearer <token>`.


## Licencia

Este proyecto es únicamente para fines académicos y no debe ser utilizado en producción sin realizar pruebas adicionales.