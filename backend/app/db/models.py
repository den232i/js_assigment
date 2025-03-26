import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, UUID, Integer, func

from app.db.base_model import Base


class WalletDB(Base):
    __tablename__ = 'wallet'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    balance = Column(Integer, default=0, nullable=False)

    create_time = Column(DateTime, server_default=func.now())
    update_time = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
