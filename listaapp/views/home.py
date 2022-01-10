# coding=utf-8
from django.shortcuts import render

from django.views.generic import *

from listaapp.models.crianca import Crianca


class HomeView(TemplateView):

    template_name = 'home.html'
    model = Crianca

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dashboard = Crianca.objects.filter(excluido=False, desativado=False ).order_by("id")
        context['dashboard'] = dashboard
        print(dashboard)
        return context

    def get(self, request, *args, **kwargs):
        # if not self.request.user.is_authenticated:
        #     return redirect(reverse_lazy('login'))
        # else:
        #     if not self.request.user.groups.filter(name = 'Administrador').exists():
        #         return redirect(reverse_lazy('chamado-meu-list'))
        return render(request,self.template_name,self.get_context_data())

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)