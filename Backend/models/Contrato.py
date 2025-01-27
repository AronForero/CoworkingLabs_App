import enum
from sqlalchemy import (
    Column, ForeignKey, Integer, String, DateTime, Enum
    )
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..database import Base


class Estado(enum.Enum):
    ACTIVO = "activo"
    INACTIVO = "inactivo"
    PENDIENTE = "pendiente"


class Contrato(Base):
    __tablename__ = "contrato"

    id_contrato = Column(Integer, primary_key=True, index=True)
    id_empresa = Column(Integer, ForeignKey("empresa.id"), nullable=False)
    empresa = relationship("empresa")
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime, nullable=False)
    estado = Column(Enum(Estado), nullable=False)
    created_at = Column(DateTime, server_default=func.now())