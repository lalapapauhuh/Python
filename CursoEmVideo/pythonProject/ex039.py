#alistamento
from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - ano

if idade > 18:
    print('Já passaram {} anos da data do seu alistamento'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(ano + 18))
elif idade < 18:
    print('Ainda faltam {} anos para você se alistar'.format(18 - idade))
    print('Seu alistamento sera em {}'.format(ano + 18))
else:
    print('Você deve se alistar este ano!')

