from sqlalchemy.orm import Session
from .models import Usuario, RegistroIoT
from .schemas import UsuarioCreate, RegistroIoTCreate

# CRUD para Usuarios
def create_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(
        nombre=usuario.nombre,
        correo=usuario.correo,
        contrasena=usuario.contrasena
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def get_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()

def update_usuario(db: Session, usuario_id: int, usuario: UsuarioCreate):
    db_usuario = get_usuario(db, usuario_id)
    if db_usuario:
        db_usuario.nombre = usuario.nombre
        db_usuario.correo = usuario.correo
        db_usuario.contrasena = usuario.contrasena
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, usuario_id: int):
    db_usuario = get_usuario(db, usuario_id)
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario

# CRUD para Registros IoT
def create_registro_iot(db: Session, registro: RegistroIoTCreate):
    db_registro = RegistroIoT(
        dispositivo=registro.dispositivo,
        valor=registro.valor,
        fecha_hora=registro.fecha_hora
    )
    db.add(db_registro)
    db.commit()
    db.refresh(db_registro)
    return db_registro

def get_registro_iot(db: Session, registro_id: int):
    return db.query(RegistroIoT).filter(RegistroIoT.id_registro == registro_id).first()

def update_registro_iot(db: Session, registro_id: int, registro: RegistroIoTCreate):
    db_registro = get_registro_iot(db, registro_id)
    if db_registro:
        db_registro.dispositivo = registro.dispositivo
        db_registro.valor = registro.valor
        db_registro.fecha_hora = registro.fecha_hora
        db.commit()
        db.refresh(db_registro)
    return db_registro

def delete_registro_iot(db: Session, registro_id: int):
    db_registro = get_registro_iot(db, registro_id)
    if db_registro:
        db.delete(db_registro)
        db.commit()
    return db_registro