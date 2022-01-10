# coding=utf-8
from datetime import date, datetime


def calculoTurma(data_nasc,mes_referencia=4):
    #Info Gerais
    data_atual = date.today()
    mes_atual = data_atual.month
    ano_atual = data_atual.year
    # data_referencia = '01/%s/%s' %(mes_referencia,data_atual.year-1)
    data_referencia = '01/%s/%s' %(mes_referencia,ano_atual)
    data_referencia = datetime.strptime(data_referencia, '%d/%m/%Y').date()
    #data_nasc=data_nasc.date()
    #B1
    if data_nasc >=  date(data_referencia.year-1, data_referencia.month, data_referencia.day):
        return 1
    elif  data_nasc >= date(data_referencia.year-2, data_referencia.month, data_referencia.day):
        return 2
    elif  data_nasc >= date(data_referencia.year-3, data_referencia.month, data_referencia.day):
        return 3
    elif data_nasc >= date(data_referencia.year -4, data_referencia.month, data_referencia.day):
        return 4
    elif  data_nasc >= date(data_referencia.year-5, data_referencia.month, data_referencia.day):
        return 5
    else:
        return 6
    #
    # if data_nasc >=  date(data_referencia.year-1, data_referencia.month, data_referencia.day):
    #     return "Bercario 1 - NASC (%s)  ----- REFERE( %s )" %(str(data_nasc), str(date(data_referencia.year-1, data_referencia.month, data_referencia.day)))
    # elif  data_nasc >= date(data_referencia.year-2, data_referencia.month, data_referencia.day):
    #     return "Bercario 2 - NASC (%s)  ----- REFERE( %s )" %(str(data_nasc), str(date(data_referencia.year-2, data_referencia.month, data_referencia.day)))
    # elif  data_nasc >= date(data_referencia.year-3, data_referencia.month, data_referencia.day):
    #     return "Maternal - NASC (%s)  ----- REFERE( %s )" %(str(data_nasc), str(date(data_referencia.year-3, data_referencia.month, data_referencia.day)))
    # elif data_nasc >= date(data_referencia.year -4, data_referencia.month, data_referencia.day):
    #     return "Jardim - NASC (%s)  ----- REFERE( %s )" %(str(data_nasc), str(date(data_referencia.year-4, data_referencia.month, data_referencia.day)))
    # elif  data_nasc >= date(data_referencia.year-5, data_referencia.month, data_referencia.day):
    #     return "Pré - NASC (%s)  ----- REFERE( %s )" %(str(data_nasc), str(date(data_referencia.year-5, data_referencia.month, data_referencia.day)))
    #