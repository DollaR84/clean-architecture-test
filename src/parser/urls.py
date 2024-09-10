from django.urls import path

from . import views


urlpatterns = [
    path('parse_and_save/', views.parse_and_save_data, name='parse_and_save_data'),
]
