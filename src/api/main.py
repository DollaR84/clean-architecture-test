from contextlib import asynccontextmanager

from config import Config

from fastapi import FastAPI

from . import upload
from . import website

from .django import DjangoRouter

from .exception_handlers import register_exception_handlers


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await app.state.dishka_container.close()


class FastAPIApp:

    def __init__(self):
        self.app: FastAPI | None = None
        self.django_router = DjangoRouter()

    def create(self, config: Config) -> FastAPI:
        self.app = FastAPI(
            title="VCBoard API",
            debug=config.api.debug,
            lifespan=lifespan,
        )

        self.app.mount("/django", self.django_router.app)
        self.app.mount("/static", self.django_router.static, name="static")

        self.app.include_router(upload.router)
        self.app.include_router(website.router)
        self.app.include_router(website.multi_router)

        register_exception_handlers(self.app)

        return self.app
