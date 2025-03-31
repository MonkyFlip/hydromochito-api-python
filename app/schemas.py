from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Esquemas para Usuarios
class UsuarioBase(BaseModel):
    nombre: str
    email: str

class UsuarioCreate(UsuarioBase):
    password: str
    id_rol: int

class UsuarioRead(UsuarioBase):
    id_usuario: int
    id_rol: int
    created_at: Optional[datetime] = None  # Campo opcional
    updated_at: Optional[datetime] = None  # Campo opcional

    class Config:
        from_attributes = True

# Esquemas para Registros IoT
class RegistroIoTBase(BaseModel):
    flujo_agua: float
    nivel_agua: float
    temp: float
    energia: str  # Cambiado de 'tipo_energia' a 'energia'
    id_usuario: int

class RegistroIoTCreate(RegistroIoTBase):
    pass

class RegistroIoTRead(RegistroIoTBase):
    id_registro: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
