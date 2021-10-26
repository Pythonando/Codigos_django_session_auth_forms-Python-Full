from django.contrib import admin
from django.http import request
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path("", lambda request: redirect('/auth/login/')),
    path('plataforma/', include('plataforma.urls')),

]
