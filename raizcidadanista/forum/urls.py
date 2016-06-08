# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from forum import views

urlpatterns = [
    url(r'^$', login_required(views.ForumView.as_view()), name='forum'),
    url(r'^diretorio/$', login_required(views.DiretorioView.as_view()), name='forum_diretorio'),
    url(r'^nao-lidos/$', login_required(views.NaoLidosView.as_view()), name='forum_nao_lidos'),
    url(r'^meu-perfil/$', login_required(views.MeuPerfilView.as_view()), name="forum_meu_perfil"),
    url(r'^pesquisa/$', login_required(views.PesquisaView.as_view()), name="forum_pesquisa"),
    url(r'^grupo/(?P<pk>\d+)/$', login_required(views.GrupoView.as_view()), name='forum_grupo'),
    url(r'^grupo/(?P<grupo_pk>\d+)/topico/add/$', login_required(views.TopicoAddView.as_view()), name='forum_topico_add'),
    url(r'^grupo/(?P<grupo_pk>\d+)/topico/(?P<pk>\d+)/$', login_required(views.TopicoView.as_view()), name='forum_topico'),
]
