from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.pedidos_models import CheckoutModel, PedidosModel
from schemas.pedidos_schema import CheckoutSchema, PedidoSchema
from core.deps import get_session


router = APIRouter()


# POST pedidos
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PedidoSchema)
async def post_pedidos(pedidos: PedidoSchema, db: AsyncSession = Depends(get_session)):
    novo_pedido = PedidosModel(checkout_id=pedidos.checkout_id)

    db.add(novo_pedido)
    await db.commit()

    return novo_pedido


# GET pedidos
@router.get('/', response_model=List[PedidoSchema])
async def get_pedidos(db: AsyncSession = Depends(get_session)):
    query = select(PedidosModel)
    result = await db.execute(query)
    pedidos = result.scalars().all()
    return pedidos


# GET pedidos por ID
@router.get('/{pedido_id}', response_model=PedidoSchema)
async def get_pedido_by_id(pedido_id: int, db: AsyncSession = Depends(get_session)):
    query = select(PedidosModel).where(PedidosModel.id == pedido_id)
    result = await db.execute(query)
    pedido = result.scalar_one_or_none()
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido


# PUT pedidos
@router.put('/{pedido_id}', response_model=PedidoSchema)    
async def put_pedido_by_id(pedido_id: int, pedido: PedidoSchema, db: AsyncSession = Depends(get_session)):
    query = select(PedidosModel).where(PedidosModel.id == pedido_id)
    result = await db.execute(query)
    pedido_db = result.scalar_one_or_none() 
    if pedido_db is None:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    for field, value in pedido.model_dump().items():
        setattr(pedido_db, field, value)
    db.add(pedido_db)
    await db.commit()
    return pedido_db


# DELETE pedidos
@router.delete('/{pedido_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_pedido_by_id(pedido_id: int, db: AsyncSession = Depends(get_session)):
    query = select(PedidosModel).where(PedidosModel.id == pedido_id)
    result = await db.execute(query)
    pedido_db = result.scalar_one_or_none()
    if pedido_db is None:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    await db.delete(pedido_db)
    await db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# POST checkout
@router.post('/checkout', status_code=status.HTTP_201_CREATED, response_model=CheckoutSchema)
async def post_checkout(checkout: CheckoutSchema, db: AsyncSession = Depends(get_session)):
    novo_checkout = CheckoutModel(status=checkout.status)
    db.add(novo_checkout)
    await db.commit()
    return novo_checkout