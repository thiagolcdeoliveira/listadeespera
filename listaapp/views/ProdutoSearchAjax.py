from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View

from ..models.produto import Produto


class ProdutoSearchAjaxView(View):
    '''
    Adiciona um pedido via AJAX.
   :URl: http://ip_servidor/pedido/cadastrar/
    '''
    template_name_json = 'includes/pesquisamultipla_json.html'
    template_mensagem = 'includes/message_json.html'

    def get(self, request,**kwargs):
        '''
        :param request:
        :param id:
        :param kwargs: id do produto
        :return: HTML do modal
        '''
        context = {}
        data = {}
        context['url'] = reverse('produto-ajax-search')
        context['campo_alterar'] = 'id_produto_utilizado'
        data['html_form'] = render_to_string(self.template_name_json, context, request=request)
        return JsonResponse(data)

    def post(self, request):
        '''
        :param self:
        :param request:
        :param id: id do produto
        :return: sucesso ou não do cadstro
        '''
        context = {}
        print("teste")
        data = dict()
        data['form_is_valid'] = False
        descricao = request.POST.get("descricao")
        context['object'] = Produto.objects.filter(
                                                  Q(descricao__contains=descricao)|Q(nome__contains=descricao)|
                                                         Q(pk__contains=descricao)
                                                         )
        context['descricao'] = descricao
        context['url'] = reverse('produto-ajax-search')
        context['campo_alterar'] = 'id_produto_utilizado'

        data['html_form'] = render_to_string(self.template_name_json, context, request=self.request)
        return JsonResponse(data)


    def form_valid(self, form):
        '''
        :param self:
        :param form: de cadastro do pedido
        :return: um JSON com as informações sobre o cadstro
        '''
        data = dict()
        context = {}
        form.save()
        data['form_is_valid'] = True
        data['html_mensagem'] = render_to_string(self.template_mensagem, context, request=self.request)
        return JsonResponse(data)

    def form_invalid(self, form):
        '''

        :param self:
        :param form: erro no form
        :return: retorna o erro no cadastro
        '''
        context = {}
        data = dict()
        data['form_is_valid'] = False
        context['form'] = form
        context['classe_css'] = 'produto_add'
        context['url'] = reverse('produto-ajax-search')
        data['html_form'] = render_to_string(self.template_name_json, context, request=self.request)
        return JsonResponse(data)