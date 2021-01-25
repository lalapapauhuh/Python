#separando unidade dezena centana etc
import itertools
n = int(input('Digite um numero entre 0 e 9999: '))
print('O numero {} tem'.format(n))
u = n //1 % 10
d = n //10 % 10
c = n //100 % 10
m = n //1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
