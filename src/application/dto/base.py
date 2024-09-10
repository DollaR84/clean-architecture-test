from dataclasses import asdict
from typing import Any


class BaseData:

    def dict(self, exclude_unset: bool = False, exclude: list | None = None) -> dict[str, Any]:
        result = asdict(self)

        if exclude_unset:
            result = {key: value for key, value in result.items() if value is not None}

        if exclude:
            result = {key: value for key, value in result.items() if key not in exclude}

        return result
