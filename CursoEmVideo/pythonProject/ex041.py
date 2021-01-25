#categoria do atleta
from datetime import date
cores = {'limpa': '\033[m',
         'ciano': '\033[37;46m',
         'azul': '\033[37;44m',
         'verde': '\033[37;42m',
         'roxo': '\033[37;45m',
         'vermelho': '\033[37;41m'

}
ano = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - ano
print('Idade: {}'.format(idade))

if  idade <= 9:
    print('Categoria: {}MIRIM{}'.format(cores['ciano'], cores['limpa']))
elif idade <= 14:
    print('Categoria: {}INFANTIL{}'.format(cores['azul'], cores['limpa']))
elif idade <= 19:
    print('Categoria: {}JÚNIOR{}'.format(cores['verde'], cores['limpa']))
elif idade <= 25:
    print('Categoria: {}SÊNIOR{}'.format(cores['roxo'], cores['limpa']))
elif idade > 25:
    print('Categoria: {}MASTER{}'.format(cores['vermelho'], cores['limpa']))
