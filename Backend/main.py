from fastapi import FastAPI
from models.Empresa import Empresa
from routers import Persona


app = FastAPI()

app.include_router(Persona.router, prefix="/api", tags=["persona"])

@app.get("/")
def read_root():
    return {"message": "¡FastAPI is working ome!"}

@app.post("/empresas/")
def create_empresa(empresa: Empresa):
    return {"message": "Empresa creada", "data": empresa}