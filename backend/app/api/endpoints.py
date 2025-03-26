from fastapi import APIRouter

from app.api.router import wallets

api_router = APIRouter()

api_router.include_router(wallets.router, prefix="/wallets", tags=["Wallets"])
