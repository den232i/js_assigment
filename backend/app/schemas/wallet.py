from datetime import datetime
from enum import StrEnum
from uuid import UUID

from pydantic import BaseModel


class OperationType(StrEnum):
    deposit = "DEPOSIT"
    withdraw = "WITHDRAW"


class Wallet(BaseModel):
    id: UUID
    balance: int

    create_time: datetime
    update_time: datetime


class WalletOperation(BaseModel):
    operation_type: OperationType
    amount: int
