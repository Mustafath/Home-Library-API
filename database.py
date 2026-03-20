from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import Annotated
from fastapi import Depends

DATABASE_URL = "sqlite+aiosqlite:///library.db"

engine = create_async_engine(DATABASE_URL)

new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]