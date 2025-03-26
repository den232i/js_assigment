from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.settings import DATABASE_URL

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for getting async session"""
    try:
        session: AsyncSession = async_session()
        yield session
    except Exception as e:
        await session.rollback()
        raise e
    finally:
        await session.close()
