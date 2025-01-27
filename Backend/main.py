from fastapi import FastAPI
from pydantic import BaseModel
from .database import Base, engine
from models.Empresa import Empresa


app = FastAPI()
# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "¡FastAPI is working ome!"}


class Empresa(BaseModel):
    id: int
    nombre: str
    nit: str

@app.post("/empresas/")
def create_empresa(empresa: Empresa):
    return {"message": "Empresa creada", "data": empresa}