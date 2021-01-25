'''class Pilha:  # vai empilhando itens novos
    def __init__(self):
        self._itens = []
    
    def adiciona(self, item):
        self._itens.append(item)
    
    def pop(self):
        try:
            return self._itens.pop() # retorna o ultimo item e o remove
        except IndexError:  # Evita erro caso a pilha esteja vazia
            return ('Pilha vazia')

    def __len__(self):  # Faz o len da lista
        return len(self._itens)
    
    def __repr__(self):  # parecido com __str__
        return f'Pilha ({self._itens})'

pilha = Pilha()
pilha.adiciona(1)
pilha.adiciona(5)
print(pilha)
print(len(pilha))
print(pilha.pop())
print(pilha.pop())
print(pilha)
print(pilha.pop())
'''
class Fila(): # Remove itens antigos a medida q novos vao entrando
    def __init__(self):
        self._itens = []

    def enqueue(self, item):
        self._itens.append(item)
    
    def dequeue(self):
        try:
            return self._itens.pop(0) # remove o primeiro item da lista
        except IndexError:
            print('Fila vazia')
    
    def __len__(self):
        return len(self._itens)
    
    def __repr__(self):
        return f'Fila ({self._itens})'