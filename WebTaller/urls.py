from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


urlpatterns = [

    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name="nosotros"),

    # GESTION USUARIOS
    path('accounts/login/', views.login, name='login'),
    path('salir', views.salir, name='salir'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)