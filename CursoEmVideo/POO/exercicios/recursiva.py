import math

def para_segundos(h):
    seg = (h*60)*60
    return int(seg)

horas = float(input('HORAS: '))
segundos = para_segundos(horas)
print(segundos)