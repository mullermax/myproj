from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')


def articles(request,year):
    return HttpResponse('O ano passado foi :' + str(year))


def lerDoBanco(nome):
    lista_nomes =[
        {'nome': 'Inaiara', 'Idade': 48},
        {'nome': 'Amandha', 'Idade': 23},
        {'nome': 'Severino', 'Idade': 54}
    ]
    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa

    return {'nome': 'Não encontra', 'Idade': 0}


def fname(request, nome):
    result = lerDoBanco(nome)
    if result['Idade'] > 0:
        return HttpResponse('A pessoa foi encontrada, ela tem: ' + str(result['Idade']) + 'Anos')
    else:
        return HttpResponse('Pessoa não encontrada')


def fname2(request, nome):
    idade = lerDoBanco(nome)['idade']
    return render(request, 'new.html', {'v_idade': idade})



