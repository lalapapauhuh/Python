import re

txt = 'O Sol na Espanha'
x = re.sub("a", "A", txt, 1)

print(x)