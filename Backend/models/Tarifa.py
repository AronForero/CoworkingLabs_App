from sqlalchemy import (
    Column, Integer, Float, String, DateTime
)
from sqlalchemy.sql import func
from ..database import Base


class Tarifa(Base):
    __tablename__ = 'tarifa'

    id_tipo_espacio = Column(Integer, primary_key=True)
    nombre_espacio = Column(String(50), nullable=False)
    tarifa_base = Column(Float, nullable=False)
    created_at = Column(DateTime, server_default=func.now())