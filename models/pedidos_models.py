from core.configs import settings
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from datetime import datetime
from typing import List, Optional

class CheckoutModel(settings.DBBaseModel):
    __tablename__ = 'checkout'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    status: bool = Column(Boolean, default=False)
    data_criacao: datetime = Column(DateTime, default=datetime.now)
    #usuario_id: int = Column(Integer, ForeignKey('usuarios.id'))
    #pedidos: Mapped[List['PedidosModel']] = relationship('PedidosModel', back_populates='checkout')
    

class PedidosModel(settings.DBBaseModel):
    __tablename__ = 'pedidos'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    checkout_id: int = Column(Integer, ForeignKey('checkout.id'))
    checkout: Mapped['CheckoutModel'] = relationship('CheckoutModel', back_populates='pedidos')
