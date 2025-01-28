from sqlalchemy import (
    Column, Integer, Float, DateTime, ForeignKey
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..database import Base


class Venta(Base):
    __tablename__ = 'venta'

    id_venta = Column(Integer, primary_key=True)
    id_empresa = Column(Integer, ForeignKey('empresa.id_empresa'), nullable=False)
    año = Column(Integer, nullable=False)
    monto = Column(Float, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    empresa = relationship("Empresa", back_populates="ventas")
