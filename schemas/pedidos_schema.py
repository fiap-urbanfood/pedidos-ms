from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel as SCBaseModel

class PedidoBase(SCBaseModel):
    checkout_id: int

class PedidoCreate(PedidoBase):
    pass

class PedidoResponse(PedidoBase):
    id: int
    
    class Config:
        orm_mode = True

class CheckoutBase(SCBaseModel):
    status: bool = False

class CheckoutCreate(CheckoutBase):
    pass

class CheckoutResponse(CheckoutBase):
    id: int
    data_criacao: datetime

    class Config:
        orm_mode = True
