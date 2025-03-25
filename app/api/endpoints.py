from fastapi import APIRouter

from api.router import wallets

api_router = APIRouter()

api_router.include_router(wallets.router, prefix="/wallets", tags=["Wallets"])
