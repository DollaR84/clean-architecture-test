from application.interactors import CreateUpload, CreateUploadFile, CreateWebsitesInfo
from application.services import UploadService

from config import Config

from dishka import from_context, Provider, Scope, provide


class ServiceProvider(Provider):
    scope = Scope.REQUEST

    config = from_context(provides=Config, scope=Scope.APP)

    @provide(scope=Scope.REQUEST)
    async def get_upload_service(
            self,
            config: Config,
            interactor_create_upload: CreateUpload,
            interactor_create_upload_file: CreateUploadFile,
            interactor_create_websites_info: CreateWebsitesInfo,
    ) -> UploadService:
        return UploadService(
            config,
            interactor_create_upload,
            interactor_create_upload_file,
            interactor_create_websites_info,
        )
