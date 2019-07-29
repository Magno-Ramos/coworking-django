from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from core.api.viewset import CoworkingViewSet
from core.views import home as core_home
from agendamentos.api.viewsets import AgendamentoViewSet
from clientes.api.viewsets import ClienteViewSet
from salas.api.viewset import SalaViewSet
from usuarios.api.viewsets import UsuarioViewSet


routers = DefaultRouter()
routers.register(r'coworkings', CoworkingViewSet, base_name='Coworking')
routers.register(r'salas', SalaViewSet, base_name='Sala')
routers.register(r'agendamentos', AgendamentoViewSet, base_name='Agendamento')
routers.register(r'clientes', ClienteViewSet, base_name='Cliente')
routers.register(r'usuarios', UsuarioViewSet, base_name='Usuario')

urlpatterns = [
    path('', core_home),
    path('admin/', admin.site.urls),
    path('api/v1/', include(routers.urls)),
    path('api-token-auth/', views.obtain_auth_token)
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
