from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import WalletDB
from app.db.session import get_db
from app.schemas.wallet import WalletOperation, OperationType

router = APIRouter()


@router.get("/<wallet_uuid>", response_model=int)
async def get_wallet_balance(
        wallet_uuid: UUID,
        db: AsyncSession = Depends(get_db)
) -> int:
    wallet_db = await db.get(WalletDB, wallet_uuid)
    if wallet_db is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f'Wallet not found'
        )

    return wallet_db.balance


@router.post("/<wallet_uuid>/operation")
async def make_operation(
        wallet_uuid: UUID,
        operation_data: WalletOperation,
        db: AsyncSession = Depends(get_db)
) -> int:
    wallet_db = await db.get(WalletDB, wallet_uuid)
    if wallet_db is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f'Wallet not found'
        )
    if operation_data.operation_type == OperationType.deposit:
        wallet_db.balance += operation_data.amount
    elif operation_data.operation_type == OperationType.withdraw:
        wallet_db.balance -= operation_data.amount

    await db.commit()

    return wallet_db.balance

