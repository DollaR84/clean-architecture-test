from dataclasses import dataclass, field
import os


@dataclass(slots=True)
class DBConfig:
    username: str = os.environ.get('POSTGRES_USER')
    password: str = os.environ.get('POSTGRES_PASSWORD')
    db_name: str = os.environ.get('POSTGRES_DB')
    host: str = os.environ.get('POSTGRES_HOST')
    port: int = os.environ.get('POSTGRES_PORT')

    debug: bool = os.environ.get("SQLALCHEMY_DEBUG", "False") == "True"

    @property
    def db_uri(self) -> str:
        return f'postgresql+asyncpg://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}'


@dataclass(slots=True)
class APIConfig:
    debug: bool = os.environ.get("FASTAPI_DEBUG", "False") == "True"
    upload_folder: str = os.environ.get("FASTAPI_UPLOAD_FOLDER")


@dataclass(slots=True)
class CsvConfig:
    delimiter: str = ';'
    quotechar: str = '|'
    url_column_name: str = "url"


@dataclass(slots=True)
class Config:
    db: DBConfig = field(default_factory=DBConfig)
    api: APIConfig = field(default_factory=APIConfig)
    csv: CsvConfig = field(default_factory=CsvConfig)
