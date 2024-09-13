from asyncio import current_task
from contextlib import asynccontextmanager
import logging
from typing import AsyncIterable

from config import Config

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, async_scoped_session
from sqlalchemy.exc import OperationalError

from .base import Base, DbConnector


class PostgresDbConnector(DbConnector):

    def __init__(self, config: Config):
        try:
            self._engine = create_async_engine(
                config.db.db_uri,
                echo=config.db.debug,
                pool_size=15,
                max_overflow=15,
            )
        except Exception as error:
            logger = logging.getLogger()
            logger.error(error, exc_info=True)
            raise ValueError("Error: failed to create engine") from error

        self._session_factory = async_sessionmaker(
            binds={Base: self._engine},
            class_=AsyncSession,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    @asynccontextmanager
    async def get_session(self) -> AsyncIterable[AsyncSession]:
        session = async_scoped_session(self._session_factory, scopefunc=current_task)()
        try:
            yield session

        except Exception as error:
            await session.rollback()
            raise OperationalError(str(error))

        finally:
            await session.aclose()
