from abc import abstractmethod
from typing import AsyncIterable, Protocol

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class DbGateway(Protocol):

    @abstractmethod
    async def get_session(self) -> AsyncIterable[AsyncSession]:
        raise NotImplementedError
