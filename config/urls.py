"""pontos_turisticos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from core.api.viewset import DocRGViewSet, PontoTuristicoViewSet
from atracoes.api.viewset import AtracoesViewSet
from enderecos.api.viewset import EnderecoViewSet
from comentarios.api.viewset import ComentarioViewSet
from avaliacoes.api.viewset import AvaliacaoViewSet
from rest_framework.authtoken.views import obtain_auth_token 
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
# Endpoints: Endpoint é a url que me guia para um recurso
router.register(r'pontoturistico', PontoTuristicoViewSet, basename='PontoTuristico')
router.register(r'doc_rg', DocRGViewSet, basename='DocRG')
router.register(r'atracoes', AtracoesViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] 


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
