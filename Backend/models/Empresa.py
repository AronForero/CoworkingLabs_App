from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class Empresa(Base):
    __tablename__ = "empresa"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, nullable=False)
    nit = Column(Integer, index=True, nullable=False)
    centro_costos = Column(String, nullable=True)
    beneficio_descuento = Column(Integer, nullable=False)
    fecha_registro = Column(DateTime, server_default=func.now())