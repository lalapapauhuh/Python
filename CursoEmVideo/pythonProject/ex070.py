#estatisticas em produtos
caro = total = barato = cont = 0
nome = str('')
fim = False
print('-'*40)
print('{: ^40}'.format('CAIXA DA LOJA'))
print('-'*40)

while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço: R$ '))
    if cont == 0 or barato > preco:
        nome = produto
        barato = preco
        cont +=1
    if preco > 100:
        caro += 1
    total += preco
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

    while continuar not in 'SN':
        continuar = str(input('Resposta Invalida. Digite apenas Sim ou Não: ')).upper().strip()[0]
        if continuar == 'N':
            break
    if continuar == 'N':
        print('-' * 40)
        print(f'Total gasto: R${total:.2f} \nProdutos que custam mais que R$100: {caro}')
        print(f'Produto mais barato: {nome}')
        break
print('Obrigado. Volte sempre!')
