import enum
from sqlalchemy import (
    Column, Integer, Float, String, DateTime, ForeignKey, Enum
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..database import Base


class EstadoPago(enum.Enum):
    PAGADO = "pagado"
    PENDIENTE = "pendiente"

class Facturacion(Base):
    __tablename__ = "facturacion"

    id_facturacion = Column(Integer, primary_key=True, index=True)
    id_empresa = Column(Integer, ForeignKey("empresa.id"), nullable=False)
    mes = Column(Integer, nullable=False)
    año = Column(Integer, nullable=False)
    monto = Column(Float, nullable=False, default=0)
    estado_pago = Column(Enum(EstadoPago), default=EstadoPago.PENDIENTE, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    empresa = relationship("empresa", back_populates="facturacion")
