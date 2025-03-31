from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException, status
from .hashing import verify_password  # Verificar contraseñas encriptadas
from ..schemas import UsuarioCreate
from ..dependencies import get_db
from sqlalchemy.orm import Session

# Configuración del JWT
SECRET_KEY = "tu_secreto_para_jwt"  # Cambia esto por un secreto más seguro
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Función para crear un token de acceso JWT
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Función para iniciar sesión con correo y contraseña
def login(db: Session, correo: str, contrasena: str):
    from ..models import Usuario  # Evitar problemas de importación circular
    usuario = db.query(Usuario).filter(Usuario.correo == correo).first()
    if not usuario or not verify_password(contrasena, usuario.contrasena):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Generar token JWT al iniciar sesión correctamente
    access_token = create_access_token(data={"sub": usuario.correo})
    return {"access_token": access_token, "token_type": "bearer"}