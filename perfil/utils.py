from datetime import datetime

from extrato.models import Valores

def calcula_total(obj,campo):
    total=0
    for i in obj:
        total += getattr(i, campo)
    return total

def calcula_equilibrio_financeiro():
    gastos_essenciais = Valores.objects.filter(data__month=datetime.now().month).filter(tipo='S').filter(categoria__essencial=True)
    gastos_nao_essenciais = Valores.objects.filter(data__month=datetime.now().month).filter(tipo='S').filter(categoria__essencial=False)

    total_gastos_essenciais=calcula_total(gastos_essenciais,'valor')
    total_gastos_não_essenciais=calcula_total(gastos_nao_essenciais,'valor')

    total =total_gastos_essenciais+total_gastos_não_essenciais

    try:
        percetual_gastos_essenciaias = (total_gastos_essenciais*100)/total
        percetual_gastos_nao_essenciaias = (total_gastos_não_essenciais*100)/total
        return percetual_gastos_essenciaias, percetual_gastos_nao_essenciaias
    except:
        return 0, 0