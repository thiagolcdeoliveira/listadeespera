# coding=utf-8
from __future__ import unicode_literals
from django.conf.urls import url

from baseapp.views.mensagemCreate import MensagemCreateView
from appusuario.views.PesquisarUserCreateAjax import PesquisarUserCreateAjaxView
from .views.crianca.criancaCreate import CriancaUsuarioCreateView
from .views.crianca.criancaDetail import CriancaDetailView
from .views.home import HomeView


from .views.crianca.criancaList import CriancaPublicaListView


urlpatterns = [

    # ---- Usuario ----#
    # url(r'^complemento-usuario/cadastrar/$', ComplementoUsuarioCreateViewMultiForms.as_view(), name='complemento-usuario-add'),
    # url(r'^complemento-usuario/(?P<pk>[0-9]+)/visualizar/$', CompletoUsuarioDetailView.as_view(), name='complemento-usuario-detail'),
    # url(r'^complemento-usuario/(?P<pk>[0-9]+)/editar/$', ComplementoUsuarioUpdateView.as_view(), name='complemento-usuario-update'),
    # url(r'^complemento-usuario/(?P<pk>[0-9]+)/excluir/$', ComplementoUsuarioDeleteView.as_view(), name='complemento-usuario-delete'),
    url(r'^$', CriancaPublicaListView.as_view(), name='home'),
    # url(r'^editais/listar/$', EditalView.as_view(), name='edital-list'),
     url(r'^crianca/cadastrar/$', CriancaUsuarioCreateView.as_view(),
        name='crianca-add'),
    # url(r'^chamado/admin/cadastrar/$', ChamadoCreateView.as_view(),
    #     name='chamado-admin-add'),
    # url(r'^chamado/listar$', ChamadoListView.as_view(),
    #     name='chamado-list'),
    # url(r'^chamado/servidor/listar$', ChamadoMeuListView.as_view(),
    #     name='chamado-meu-list'),
    url(r'^lista-publica/$', CriancaPublicaListView.as_view(), name='crianca-publica-list'),
    url(r'^coordenacao/lista-publica/(?P<pk>[\d\-]+)/$', CriancaPublicaListView.as_view(), name='crianca-publica-list-admin'),
    url(r'^crianca/visualizar/(?P<pk>[\d\-]+)/$', CriancaDetailView.as_view(),
        name='crianca-detail'),
    # url(r'^chamado/(?P<pk>[\d\-]+)/visualizar/$', ChamadoUsuarioDetailView.as_view(),
    #     name='chamado-usuario-detail'),
    # #
    # url(r'^chamado/atualizar/(?P<pk>[\d\-]+)/$', ChamadoUpdateView.as_view(),
    #     name='chamado-update'),
    # url(r'^chamado/admin/atualizar/(?P<pk>[\d\-]+)/$', ChamadoAdminUpdateView.as_view(),
    #     name='chamado-admin-update'),
    # url(r'^chamado/gerar/qrcode/(?P<pk>[\d\-]+)/$', ChamadoQrcodeView.as_view(),
    #     name='chamado-gera-qrcode'),
    #
    # url(r'^chamado/excluir/(?P<pk>[\d\-]+)/$', ChamadoCreateView.as_view(),
    #     name='chamado-delete'),
    # url(r'^chamado/fechar/(?P<pk>[\d\-]+)', ChamadoFecharView.as_view(),
    #     name='chamado-fechar'),
    # url(r'^chamado/abrir/(?P<pk>[\d\-]+)', ChamadoAbrirView.as_view(),
    #     name='chamado-abrir'),
    # url(r'^chamado/usuario/atualizar/(?P<pk>[\d\-]+)/$', ChamadoUpdateView.as_view(),
    #     name='chamado-usuario-update'),
    # url(r'^chamado/atendimento/iniciar/(?P<pk>[\d\-]+)/$', ChamadoIniciarUpdateView.as_view(),
    #     name='chamado-iniciar'),
    #
    # url(r'^chamado/servidor/pesquisar/$', PesquisarUserCreateAjaxView.as_view(),
    #     name='user-servidor-pesquisar'),
    # url(r'^chamado/mensagem/cadastrar/(?P<pk>[\d\-]+)/$', MensagemCreateView.as_view(),
    #     name='mensagem-chamado-add'),
    # url(r'^chamado/propriedade/(?P<pk>[\d\-]+)/$', ChamadoListView.as_view(),
    #     name='chamado-propriedade-history'),

]
