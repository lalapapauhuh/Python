#ano bissexto
from datetime import date
ano = int(input("Digite seu ano: "))
if ano == 0:
    ano = date.today().year
if ano % 100 == 0 and ano % 400 != 0 or ano % 4 != 0:
    print('O ano {} não é bissexto.'.format(ano))
else:
    print('O ano {} é bissexto.'.format(ano))