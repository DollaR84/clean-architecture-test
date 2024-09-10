from importlib.util import find_spec
import os

from django.core.wsgi import get_wsgi_application

from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles


class DjangoRouter:

    def __init__(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vcboard.settings")

        self.application = get_wsgi_application()

    @property
    def app(self):
        return WSGIMiddleware(self.application)

    @property
    def static(self):
        return StaticFiles(
            directory=os.path.normpath(
                os.path.join(find_spec("django.contrib.admin").origin, "..", "static")
            )
        )
