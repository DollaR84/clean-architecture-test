import logging

from api import FastAPIApp

import coloredlogs

from config import Config

from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka

from providers import AppProvider, DBProvider, ServiceProvider

import uvicorn


def create_app():
    coloredlogs.install()
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s  %(process)-7s %(module)-20s %(message)s',
    )

    config = Config()
    app = FastAPIApp().create(config)

    container = make_async_container(
        AppProvider(),
        DBProvider(),
        ServiceProvider(),
        context={Config: config},
    )

    setup_dishka(container, app)
    return app


if __name__ == "__main__":
    uvicorn.run(create_app(), host="0.0.0.0", port=8000, lifespan="on")
