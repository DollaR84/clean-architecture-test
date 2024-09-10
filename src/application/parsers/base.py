from __future__ import annotations

from abc import ABC, abstractmethod

from .types import ParserType


class BaseParser(ABC):
    _parsers: dict[str, BaseParser] = {}

    def __init_subclass__(cls, **kwargs):
        name = cls.__name__.replace("Parser", "").lower()
        if name not in cls._parsers:
            cls._parsers[name] = cls

    @classmethod
    def get_parser(cls, parser_type: ParserType) -> BaseParser:
        return cls._parsers.get(parser_type.value)

    def __init__(self, html: str):
        self.html: str = html

    def remove_duplicates(self, x: list[str]):
        return list(set(x))

    @abstractmethod
    def get(self):
        raise NotImplementedError
