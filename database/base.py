from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import registry
from attr import define
from config import settings
entity = define(slots=False, kw_only=True)

mapper_registry = registry()


class SqlAlchemyRepo:
    # async def __init__(self):
    #     self.session = await self.get_session()

    async def get_session(self) -> AsyncSession:
        async_engine = create_async_engine(
            url=settings.DATABASE_URL_POSTGRES
        )
        session = async_sessionmaker(async_engine)
        return session(expire_on_commit=False)
        # async with session(expire_on_commit=False) as s:
        #     yield s

    async def commit(self):
        await self.session.commit()
