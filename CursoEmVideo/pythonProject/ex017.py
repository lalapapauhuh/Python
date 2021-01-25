#calculo da hipotenusa
from math import sqrt
A = float(input('Digite o cateto oposto: '))
B = float(input('Digite o cateto adjacente: '))
C = (A**2) + (B**2) #ou C = math.hypot(A, B)
print('A hipotenusa é {:.2f}'.format(sqrt(C)))
