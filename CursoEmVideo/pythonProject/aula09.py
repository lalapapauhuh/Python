''' Manipulações de cadeias de texto
len(), count(), find(), replace(), upper(), lower(), capitalize(),
title(),strip(), join().
 '''
import itertools

'''Fatiamento
frase = str ('Curso em Vídeo Python')
print(frase[9::3])'''

'''analise: 
len: conta quantos caracters sao usados, incluindo espaços "print(len(frase))"
count: conta quantas vzs algum caractere apareceu "print(frase.count('a'))/(frase.count('a,0, 13'))" "
find: parece o "encontrar na pagina" mas mostra a posição q onde começa "print(frase.find('deo'))"
in: procura alguma palavra ou caracter na frase, retorna true ou false.
'''

'''Transformacao 
replace:   troca uma palavra por outra "print(frase.replace('Python', 'Android'))"
upper()/lower(): deixa tudo em maiusculo, ou minusculo 
capitalize():  deixa td em minusculo, e só o primeiro fica maiusculo.
tittle():  analisa qnts palavras existem com base nos espaços, e deixa a primeira letra de cada maiuscula
strip():  remove todos espaços inuteis, no começo e no fim, caso haja
rstrip()/lsptrip(): remove somente os espaços do final/começo
enumerate () coloca o numero da posicao do dado dentro da tupla/lista/dicionario
sorted() organiza em ordem alfabetica/numerica
'''

'''Divisão
split(): onde tem espaços ele cria uma divisao, assim os "indices" sao zerados a cada espaço, faz uma lista virar varias
'''

'''Junção
join: faz virar uma unica frase/palavra "
'''

frase = str ('Curso em Vídeo Python')
print(''.join(frase))
