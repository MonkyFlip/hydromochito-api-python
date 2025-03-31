from sqlalchemy import Column, Integer, String, BigInteger, DECIMAL, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "tb_usuarios"
    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)  # Cambiar "correo" a "email"
    password = Column(String, nullable=False)
    id_rol = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)

class RegistroIoT(Base):
    __tablename__ = "tb_registros_iot"
    id_registro = Column(Integer, primary_key=True, index=True)
    flujo_agua = Column(DECIMAL, nullable=False)
    nivel_agua = Column(DECIMAL, nullable=False)
    temp = Column(DECIMAL, nullable=False)
    energia = Column(String, nullable=False)  # Cambiado de 'tipo_energia' a 'energia'
    id_usuario = Column(BigInteger, ForeignKey("tb_usuarios.id_usuario"), nullable=False)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)
