from django.urls import path
from .models import Tarefa, Grupos, Sub_Grupos
from .views import Logar, Registrar, ListaTarefa, TodasTarefas, VisualizaGrupo, VisualizaSubGrupo, Criar, CriarGrupo, CriarSubGrupo, Atualizar, \
    AtualizarGrupo, AtualizarSubGrupo, Apagar, ApagarGrupo, ApagarSubGrupo, MostraTarefaGrupo, MostraSubGrupo
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('tarefas/', ListaTarefa.as_view(), name='tarefas'),
    path('login/', Logar.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('registrar/', Registrar.as_view(), name='registrar'),
    path('todas/', TodasTarefas.as_view(), name='completo'),
    path('', VisualizaGrupo.as_view(), name='grupos'),
    path('subgrupos/', VisualizaSubGrupo.as_view(), name='subgrupos'),
    path('criar/', Criar.as_view(), name='criar'),
    path('criar_grupo/', CriarGrupo.as_view(), name='criar_grupo'),
    path('criar_subgrupo/', CriarSubGrupo.as_view(), name='criar_subgrupo'),
    path('atualizar/<int:pk>/', Atualizar.as_view(), name='atualizar'),
    path('atualizar_grupos/<int:pk>/', AtualizarGrupo.as_view(), name='atualizar_grupos'),
    path('atualizar_subgrupos/<int:pk>/', AtualizarSubGrupo.as_view(), name='atualizar_subgrupos'),
    path('apagar/<int:pk>/', Apagar.as_view(), name='apagar'),
    path('apagar_grupo/<int:pk>/', ApagarGrupo.as_view(), name='apagar_grupo'),
    path('apagar_subgrupo/<int:pk>/', ApagarSubGrupo.as_view(), name='apagar_subgrupo'),
    path('mostra_tarefa_grupo/<int:pk>/', MostraTarefaGrupo.as_view(), name='mostra_tarefa_grupo'),
    path('mostra_subgrupo/<int:pk>/', MostraSubGrupo.as_view(), name='mostra_subgrupo'),
]
