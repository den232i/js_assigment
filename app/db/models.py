import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, UUID, Integer, ForeignKey, func
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from sqlalchemy.orm import mapped_column

from db.base_model import Base
from schemas.wallet import OperationType


class WalletDB(Base):
    __tablename__ = 'wallet'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    balance = Column(Integer, default=0, nullable=False)

    create_time = Column(DateTime, server_default=func.now())
    update_time = Column(DateTime, default=datetime.now(), onupdate=datetime.now())


class OperationDB(Base):
    __tablename__ = 'operation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(PgEnum(OperationType), nullable=False)
    amount = Column(Integer, nullable=False)

    to_wallet_id = mapped_column(ForeignKey('wallet.id'), nullable=True)

    create_time = Column(DateTime, server_default=func.now())


