from typing import Optional
from datetime import datetime

from pydantic import BaseModel as SCBaseModel


class CheckoutSchema(SCBaseModel):
    id: Optional[int]
    status: bool
    #data_criacao: datetime

    class Config:
        orm_mode = True


class PedidoSchema(SCBaseModel):
    id: Optional[int]
    checkout_id: int

    class Config:
        orm_mode = True
