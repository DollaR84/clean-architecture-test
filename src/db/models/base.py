from typing import Any

import sqlalchemy.orm as so

from utils.text import paschal_case_to_snake_case


class BaseDBModel:

    @so.declared_attr
    def __tablename__(self):
        return paschal_case_to_snake_case(self.__name__) + "s"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)

    def __str__(self):
        return f"{self.__class__.__name__} #{self.id}"

    def __repr__(self):
        return f"{self.__class__.__name__} #{self.id}"

    def dict(self, exclude_unset: bool = False, exclude: list | None = None) -> dict[str, Any]:
        result = {c.name: getattr(self, c.name) for c in self.__table__.columns}

        if exclude_unset:
            result = {key: value for key, value in result.items() if value is not None}

        if exclude:
            result = {key: value for key, value in result.items() if key not in exclude}

        return result
