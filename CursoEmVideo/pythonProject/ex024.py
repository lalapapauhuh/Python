#palavra santo
import itertools

cidade = str(input('Digite o nome da sua cidade: '))
cidade = cidade.lower()

s = cidade.find('santo')
if s < 0:
    print('Sua cidade não possui Santo no nome!')
elif s >=0 :
    print('Sua cidade possui Santo no nome!')

