from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..database import Base


class Persona(Base):
    __tablename__ = 'persona'

    id_persona = Column(Integer, primary_key=True, autoincrement=True)
    id_empresa = Column(Integer, ForeignKey('empresa.id_empresa'), nullable=True)
    cedula = Column(String(20), nullable=False)
    nombre = Column(String(100))
    correo = Column(String(100), nullable=False, unique=True)
    telefono = Column(String(15))
    numero_id_huella = Column(String(50), unique=True, nullable=True)
    fecha_registro = Column(DateTime, server_default=func.now())

    empresa = relationship("Empresa", back_populates="personas")