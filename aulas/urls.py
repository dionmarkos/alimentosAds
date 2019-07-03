from django.urls import path, include
from . import views

app_name = "aulas"

urlpatterns = [
    path('criarNovaAula/', views.criarNovaAula, name = 'criarNovaAula'),
    path('', views.aulasList, name = 'aulasList'),
    path('aula/<int:pk>', views.aula, name = 'aula'),
    path('criarCurso/', views.criarCurso, name = 'criarCurso'),
    # path('', views.index, name='index'),
    # path('aula', views.aula, name='aula'),
    path('ajuda', views.ajuda, name='ajuda'),
    path('consultas', views.consultas, name='consultas'),
    path('cursos', views.cursos, name='cursos'),
    # path('recuperarsenha', views.recuperarsenha, name='recuperarsenha'),

]
