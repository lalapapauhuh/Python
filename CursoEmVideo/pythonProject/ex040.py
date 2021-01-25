#média e situação do aluno
cores = {'limpa':'\033[m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         'verde': '\033[32m'
}
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2

if media >= 7.0:
    print('{}Sua média foi de {:.2f} Você está Aprovado!{}'.format(cores['verde'], media, cores['limpa']))
elif media >= 5.0 and media < 7.0:
    print('{}Sua média foi de {:.2f} Você está em Recuperação.{}'.format(cores['amarelo'], media, cores['limpa']))
elif media < 5.0:
    print('{}Sua média foi de {:.2f} Você está foi Reprovado.{}'.format(cores['vermelho'],media, cores['limpa']))
