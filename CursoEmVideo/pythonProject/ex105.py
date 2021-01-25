# Analisando e gerando dicionarios
def notas(* nums, sit=False):
    resposta = {}
    resposta['Total'] = len(nums)
    resposta['Maior'] = max(nums)
    resposta['Menor'] = min(nums)
    resposta['Média'] = sum(nums)/len(nums)
    if sit == True:
        if resposta['Média'] > 6:
            resposta['Situação'] = 'Boa'
        elif resposta['Média'] >= 5:
            resposta['Situação'] = 'Regular'
        else:
            resposta['Situação'] = 'Ruim'
    return resposta


# Programa principal
resp = notas(5.0, 7.5, 8.5, 9.0, sit=True)
print(resp)

