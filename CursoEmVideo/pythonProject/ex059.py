#menu de opções
from time import sleep
cores = { 'limpa': '\033[m',
          'vermelho': '\033[31m',
          'branco': '\033[7;30m'
}
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo valor: '))
fim = False

while not fim:
    print(' 1 - Somar\n 2 - Multiplicar\n 3 - Qual é maior\n 4 - Novos números\n 0 - Sair')
    operacao = int(input('{}Digite sua opção{} '.format(cores['branco'], cores['limpa'])))
    if operacao == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
        print('='*40)
    elif operacao == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1*n2))
        print('=' * 40)
    elif operacao == 3:
        if n1 > n2:
            print('Entre {} e {} o maior número é {}'.format(n1, n2, n1))
            print('=' * 40)
        elif n2 > n1:
            print('Entre {} e {} o maior número é {}'.format(n1, n2, n2))
            print('=' * 40)
        else:
            print('Os valores são iguais!!')
            print('=' * 40)
    elif operacao == 4:
        n1 = int(input('Digite novamente o primeiro número: '))
        n2 = int(input('Digite  novamente o segundo valor: '))
        print('=' * 40)
    elif operacao == 0:
        print('=' * 40)
        print('{}Finalizando programa...{}'.format(cores['branco'], cores['limpa']))
        sleep(2)
        print('='*10, 'Programa finalizado com sucesso!', '='*10)
        fim = True
    else:
        print('{}Opção invalida. Tente novamente...{}'.format(cores['vermelho'], cores['limpa']))
