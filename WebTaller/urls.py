from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


urlpatterns = [

    path('index', views.index, name='index'),

    # GESTION USUARIOS
    path('login', views.login, name='login'),
    path('salir', views.salir, name='salir'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)