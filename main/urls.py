"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from suap.views import index, Informatica, Alimentos, Apicultura, ADS, Detalhe, Cadastro
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('informatica/', Informatica, name='informatica'),
    path('alimentos/', Alimentos, name='alimentos'),
    path('apicultura/', Apicultura, name='apicultura'),
    path('ads/', ADS, name='ads'),
    path('aluno/<int:aluno_id>', Detalhe, name='detalhes_aluno'),
    path('cadastro/', Cadastro, name='cadastro'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)