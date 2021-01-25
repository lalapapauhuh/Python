# função calcular se o voto é obrigatorio

def idade(a):
    from datetime import date
    return date.today().year - a


def voto(i):
    if i < 16:
        return 'Negado'
    elif i > 18 and i < 65:
        return 'Obrigatório'
    elif i >= 16 or i >= 65:
        return 'Opcional'


ano = int(input('Em que ano você nasceu? '))
idade(ano) # Calcula apenas a idade
situacao = voto(idade(ano)) # situacao recebe o resultado da funcao voto, q tem como paramentro
# a idade da pessoa, calculada por outra função.
print(f'Você tem {idade(ano)} anos: Voto {situacao}.')
