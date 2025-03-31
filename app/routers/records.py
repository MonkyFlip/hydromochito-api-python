from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..crud import create_registro_iot, get_registro_iot, update_registro_iot, delete_registro_iot
from ..models import RegistroIoT
from ..schemas import RegistroIoTCreate, RegistroIoTRead

router = APIRouter(
    prefix="/registros",
    tags=["registros"],
    responses={404: {"description": "Registro no encontrado"}}
)

@router.post("/", response_model=RegistroIoTRead)
def crear_registro(registro: RegistroIoTCreate, db: Session = Depends(get_db)):
    if registro.energia not in ["solar", "electricidad"]:
        raise HTTPException(status_code=400, detail="El campo 'energia' solo puede ser 'solar' o 'electricidad'")
    return create_registro_iot(db=db, registro=registro)


@router.get("/{registro_id}", response_model=RegistroIoTRead)
def ver_registro(registro_id: int, db: Session = Depends(get_db)):
    registro = get_registro_iot(db=db, registro_id=registro_id)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return registro

@router.get("/", response_model=list[RegistroIoTRead])
def listar_registros(db: Session = Depends(get_db)):
    registros = db.query(RegistroIoT).all()
    return registros

@router.delete("/{registro_id}", response_model=dict)
def eliminar_registro(registro_id: int, db: Session = Depends(get_db)):
    registro = get_registro_iot(db=db, registro_id=registro_id)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    delete_registro_iot(db=db, registro_id=registro_id)
    return {"mensaje": "Registro eliminado exitosamente"}