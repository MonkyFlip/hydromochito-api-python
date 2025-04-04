from passlib.context import CryptContext

# Configuración de bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Función para encriptar contraseñas
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Función para verificar contraseñas
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)