#conversor numerico
cores = {'limpar': '\033[m',
         'vermelho': '\033[41m'
}
num = int(input('Digite um número inteiro: '))
print('Digite o número da opção que você deseja converter:\n 1 - Binário\n 2 - Octal\n 3 - Hexadecimal')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} em binário é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} em octal é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('{}Opcão Invalida!!!{}'.format(cores['vermelho'], cores['limpar']))