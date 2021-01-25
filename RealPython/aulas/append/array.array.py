from array import array
from collections import deque

my_array = array('f', [1.5, 2.0, 3.8])
my_array.append(9)
print(my_array)

deck = deque([1, 'a', 3.0])
print(deck)
deck.append('b')
print(deck)
deck.appendleft(-3)
print(deck)
deck.pop() # remove o 'b'
deck.popleft() # remove o -3
print(deck)