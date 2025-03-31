from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..crud import create_usuario, get_usuario, update_usuario, delete_usuario
from ..models import Usuario
from ..schemas import UsuarioCreate, UsuarioRead

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
    responses={404: {"description": "Usuario no encontrado"}}
)

@router.post("/", response_model=UsuarioRead)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return create_usuario(db=db, usuario=usuario)

@router.get("/{usuario_id}", response_model=UsuarioRead)
def ver_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = get_usuario(db=db, usuario_id=usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.get("/", response_model=list[UsuarioRead])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return usuarios

@router.delete("/{usuario_id}", response_model=dict)
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = get_usuario(db=db, usuario_id=usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    delete_usuario(db=db, usuario_id=usuario_id)
    return {"mensaje": "Usuario eliminado exitosamente"}