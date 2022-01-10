# coding=utf-8
from __future__ import unicode_literals

from django.conf.urls import url

from baseapp.views.ContadorGerarAjax import ContadorGerarAjaxView
from listaapp.views.EnderecoCreateAjax import EnderecoCreateAjaxView
from listaapp.views.EquipamentoSearchAjax import EquipamentoSearchAjaxView
from baseapp.views.GraficoGerarAjax import GraficoGerarAjaxView
from baseapp.views.ListaGerarAjax import ListaGerarAjaxView
from listaapp.views.ProdutoSearchAjax import ProdutoSearchAjaxView
from appusuario.views.PropriedadeCreateAjax import PropriedadeCreateAjaxView
from appusuario.views.PropriedadeSearchAjax import PropriedadeSearchAjaxView
from listaapp.views.CeiCreateAjax import CeiCreateAjaxView
from baseapp.views.TabelaGerarAjax import TabelaGerarAjaxView
from appusuario.views.TipoPropriedadeCreateAjax import TipoPropriedadeCreateAjaxView

from baseapp.views.dashboard.dashboardCreate import DashboardCreateView
from baseapp.views.dashboard.dashboardDelete import DashboardDeleteView, DashboardActiveView, DashboardDesativeView
from baseapp.views.dashboard.dashboardDetail import DashboardDetailView
from baseapp.views.dashboard.dashboardListView import DashboardMeuListView
from baseapp.views.dashboard.dashboard import DashboardView
from baseapp.views.dashboard.dashboardUpdate import DashboardUpdateView
from baseapp.views.grafico.graficoDetail import GraficoDetailView
from baseapp.views.grafico.graficoList import GraficoListView
from baseapp.views.graficoCreateAjax import GraficoCreateAjaxView
from baseapp.views.notificacao import NotificacaoView
from baseapp.views.notificacaoList import NotificacaoMeuListView
from baseapp.views.grafico.graficoCreate import GraficoCreateView
from baseapp.views.propriedade.propriedadeCreate import PropriedadeCreateView
from baseapp.views.propriedade.propriedadeDetail import PropriedadeDetailView
from baseapp.views.propriedade.propriedadeList import PropriedadeListView, PropriedadeMeuListView
from baseapp.views.propriedade.propriedadeUpadate import PropriedadeUpdateView

urlpatterns = [

    # Setor
    url(r'^cei/cadastrar/ajax/', CeiCreateAjaxView.as_view(),
        name='cei-add'),


    #Dashboard
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^grafico/gerar/ajax/(?P<pk>[\d\-]+)/', GraficoGerarAjaxView.as_view(),
        name='grafico-gerar'),
    url(r'^contador/gerar/ajax/(?P<pk>[\d\-]+)/', ContadorGerarAjaxView.as_view(),
        name='contador-gerar'),
    url(r'^tabela/gerar/ajax/(?P<pk>[\d\-]+)/', TabelaGerarAjaxView.as_view(),
        name='tabela-gerar'),
    url(r'^lista/gerar/ajax/(?P<pk>[\d\-]+)/', ListaGerarAjaxView.as_view(),
        name='lista-gerar'),

    url(r'^notificacao/(?P<pk>[\d\-]+)/', NotificacaoView.as_view(),
        name='notificacao'),
    url(r'^notificacao/usuario/listar/', NotificacaoMeuListView.as_view(),
        name='notificacao-meu-list'),

    # propriedade
    url(r'^propriedade/cadastrar/ajax/', PropriedadeCreateAjaxView.as_view(),
        name='propriedade-ajax-add'),
    url(r'^propriedade/pesquisar/$', PropriedadeSearchAjaxView.as_view(),
        name='propriedade-search'),

    #grafico
    url(r'^grafico/cadastrar/$', GraficoCreateView.as_view(),
        name='grafico-add'),
    url(r'^grafico/testar/$', GraficoCreateAjaxView.as_view(),
        name='grafico-testar'),
    url(r'^grafico/listar/$', GraficoListView.as_view(),
        name='grafico-listar'),
    url(r'^grafico/visualizador/(?P<pk>[\d\-]+)/$', GraficoDetailView.as_view(),
        name='grafico-detail'),

    #dashboard
    url(r'^dashboard/meusgraficos/listar/$', DashboardMeuListView.as_view(),
        name='dashboard-meu-listar'),
    url(r'^dashboard/visualizador/(?P<pk>[\d\-]+)/$', DashboardDetailView.as_view(),
        name='dashboard-detail'),
    url(r'^dashboard/cadastrar/$', DashboardCreateView.as_view(),
        name='dashboard-add'),
    url(r'^dashboard/delete/(?P<pk>[\d\-]+)/$', DashboardDeleteView.as_view(),
        name='dashboard-delete'),
    url(r'^dashboard/desativar/(?P<pk>[\d\-]+)/$', DashboardDesativeView.as_view(),
        name='dashboard-desative'),
    url(r'^dashboard/active/(?P<pk>[\d\-]+)/$', DashboardActiveView.as_view(),
        name='dashboard-active'),
    url(r'^dashboard/update/(?P<pk>[\d\-]+)/$', DashboardUpdateView.as_view(),
        name='dashboard-update'),

    #propriedade
    url(r'^propriedade/cadastrar/$', PropriedadeCreateView.as_view(),
        name='propriedade-add'),
    url(r'^propriedade/visualizar/(?P<pk>[\d\-]+)/$', PropriedadeDetailView.as_view(),
        name='propriedade-detail'),
    url(r'^propriedade/atualizar/(?P<pk>[\d\-]+)/$', PropriedadeUpdateView.as_view(),
        name='propriedade-update'),
    url(r'^propriedade/minhaspropriedades/listar/$', PropriedadeMeuListView.as_view(),
        name='propriedade-meu-listar'),
    url(r'^propriedade/listar/$', PropriedadeListView.as_view(),
        name='propriedade-listar'),
    url(r'^propriedade/historico/$', PropriedadeListView.as_view(),
        name='propriedade-history'),
    #tipo propriedade
    url(r'^propriedade/ajax/cadastrar/$', TipoPropriedadeCreateAjaxView.as_view(),
        name='tipo-propriedade-ajax-add'),


    # endereco
    url(r'^endereco/ajax/cadastrar/$', EnderecoCreateAjaxView.as_view(),
        name='endereco-ajax-add'),

    # equipamento
    url(r'^equipamento/ajax/search/$', EquipamentoSearchAjaxView.as_view(),
        name='equipamento-ajax-search'),

    # produto
    url(r'^produto/ajax/search/$', ProdutoSearchAjaxView.as_view(),
        name='produto-ajax-search'),
]
