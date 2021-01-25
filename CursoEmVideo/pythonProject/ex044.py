#gerenciador de pagamentos
from time import sleep
cores = {'limpa': '\033[m',
         'branco': '\033[7;30m',
         'vermelho':'\033[31m'
         }

print('='*8, 'SIMULADOR DE LOJAS','='*8)
valor = float(input('Digite o valor total gasto: R$ '))

print('\nSELECIONE A FORMA DE PAGAMENTO')
print(' 1 - À vista dinheiro/cheque\n 2 - À vista cartão\n 3 - 2x no cartão\n 4 - 3x ou mais no cartão')
opcao = int(input('Digite o número da opção: ')) #recebe o numero da opcao acima

print('{}PROCESSANDO...{}'.format(cores['branco'], cores['limpa']))
sleep(2) #faz o programa esperar 2 segundos

if opcao == 1:
    novo = valor - (valor*10/100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, novo))
elif opcao == 2:
    novo = valor - (valor*5/100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, novo))
elif opcao == 3:
    parcela = valor/2
    print('Sua compra de R${:.2f} será parcelada em 2x de R${:.2f}'.format(valor, parcela))
elif opcao == 4:
    novo = valor + (valor * 20 / 100)
    parcela = (int(input('Em quantas vezes será parcelado? ')))
    totalparcela = novo/parcela
    print('Sua compra de R${:.2f} será parcelada em {} vezes de R${:.2f} somando juros'.format(valor, parcela, totalparcela))
    print('Sua compra total de R${:.2f} vai custar R${:.2f} no final'.format(valor, novo))
else:
    print('{}Opcão invalida! Tente novamente.{}'.format(cores['vermelho'], cores['limpa']))
    