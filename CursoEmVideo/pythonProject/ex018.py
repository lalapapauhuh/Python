#calculo do seno cosseno e tangente de um angulo
import math
n = float(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tang =math.tan(math.radians(n))
print('O ângulo de {:.2f} graus tem: \n Seno: {:.2f}\n Cosseno {:.2f}\n Tangente: {:.2f}'.format(n, sen, cos, tang))