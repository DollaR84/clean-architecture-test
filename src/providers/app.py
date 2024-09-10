from application import interactors

from dishka import Provider, Scope, provide


class AppProvider(Provider):

    create_upload_file_interactor = provide(interactors.CreateUploadFile, scope=Scope.REQUEST)

    create_websites_interactor = provide(interactors.CreateWebsitesInfo, scope=Scope.REQUEST)
    get_websites_interactor = provide(interactors.GetWebsitesInfo, scope=Scope.REQUEST)
    get_website_interactor = provide(interactors.GetWebsiteInfo, scope=Scope.REQUEST)
    update_website_interactor = provide(interactors.UpdateWebsiteInfo, scope=Scope.REQUEST)
    delete_website_interactor = provide(interactors.DeleteWebsiteInfo, scope=Scope.REQUEST)
