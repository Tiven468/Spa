from django.urls import path
from django.shortcuts import render
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.adminbase, name='adminbase'),
    path('listausuarios', views.listausuarios, name='listausuarios'),
    path('adminpage/', lambda request: render(request, 'usuarios/admin.html'), name='adminpage'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('cuenta/', views.cuenta, name='cuenta'),
    path('agendar/', views.agendar, name='agendar'),
    path('agregarservicio/', views.agregarservicio, name='agregarservicio'),
    path('servicios/', views.lista_servicios, name='lista_servicios'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)