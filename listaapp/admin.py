from django.contrib import admin

# Register your models here.
from listaapp.models.cei import Cei
from listaapp.models.crianca import Crianca
from listaapp.models.turma import Turma

admin.site.register(Crianca)
admin.site.register(Cei)
admin.site.register(Turma)
