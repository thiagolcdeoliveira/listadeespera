from django.contrib import admin

# Register your models here.

from baseapp.models.dashboard import Dashboard
from baseapp.models.email import ConfiguracaoEmail
from baseapp.models.grafico import Grafico
from baseapp.models.notificacao import Notificacao
from baseapp.models.settings import Settings
from baseapp.models.tamanho import Tamanho
from baseapp.models.tipo_grafico import TipoGrafico
from baseapp.models.tipo_notificacao import TipoNotificacao



admin.site.register(Dashboard)
admin.site.register(Grafico)
admin.site.register(TipoGrafico)
admin.site.register(Tamanho)


admin.site.register(Notificacao)
admin.site.register(Settings)
admin.site.register(TipoNotificacao)



admin.site.register(ConfiguracaoEmail)
