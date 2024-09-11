from application import interfaces

from config import Config

from db import PostgresDbGateway
from db import gateways
from db.base import DbGateway

from dishka import from_context, Provider, Scope, provide


class DBProvider(Provider):
    scope = Scope.REQUEST

    config = from_context(provides=Config, scope=Scope.APP)

    @provide(scope=Scope.REQUEST)
    async def get_db(self, config: Config) -> DbGateway:
        return PostgresDbGateway(config)

    @provide(scope=Scope.REQUEST)
    async def get_websites_info(self, db: DbGateway) -> interfaces.GetWebsitesInfo:
        async with db.get_session() as session:
            return gateways.GetWebsitesInfo(session)

    @provide(scope=Scope.REQUEST)
    async def get_website_info(self, db: DbGateway) -> interfaces.GetWebsiteInfo:
        async with db.get_session() as session:
            return gateways.GetWebsiteInfo(session)

    @provide(scope=Scope.REQUEST)
    async def create_websites_info(self, db: DbGateway) -> interfaces.CreateWebsitesInfo:
        async with db.get_session() as session:
            return gateways.CreateWebsitesInfo(session)

    @provide(scope=Scope.REQUEST)
    async def update_website_info(self, db: DbGateway) -> interfaces.UpdateWebsiteInfo:
        async with db.get_session() as session:
            return gateways.UpdateWebsiteInfo(session)

    @provide(scope=Scope.REQUEST)
    async def delete_website_info(self, db: DbGateway) -> interfaces.DeleteWebsiteInfo:
        async with db.get_session() as session:
            return gateways.DeleteWebsiteInfo(session)

    @provide(scope=Scope.REQUEST)
    async def create_upload_file(self, db: DbGateway) -> interfaces.CreateUploadFile:
        async with db.get_session() as session:
            return gateways.CreateUploadFile(session)

    @provide(scope=Scope.REQUEST)
    async def create_upload(self, db: DbGateway) -> interfaces.CreateUpload:
        async with db.get_session() as session:
            return gateways.CreateUpload(session)
