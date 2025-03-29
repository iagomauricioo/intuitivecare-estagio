from fastapi import APIRouter
from api.v1.endpoints import operadoras

api_router = APIRouter()
api_router.include_router(operadoras.router, prefix="/operadoras", tags=["operadoras"])