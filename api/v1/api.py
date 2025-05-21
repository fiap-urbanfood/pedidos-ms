from fastapi import APIRouter
from api.v1.endpoints import pedidos, auth

api_router = APIRouter()
api_router.include_router(pedidos.router, prefix="/pedidos", tags=["pedidos"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
