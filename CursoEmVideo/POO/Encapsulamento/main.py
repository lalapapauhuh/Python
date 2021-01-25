# Encapsulamento deixa privado alguns dados classe,
#afim de proteger o codigo/osdados
'''
Em outras linguagens usa-se public protected e private
public, protected, private

ja no python se usa   _   e __  
_   =  protected (public _)
__  =  private (_NOMEDACLASSE__nomeAtributo)

'''

class BaseDeDados:
    def __init__(self):
        self.__dados = {}


    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
    

    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)


    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Cássio')
bd.inserir_cliente(2, 'Maria')
bd.__dados = 'Outra coisa'
# print(bd.__dados) Assim mostrará 'Outra coisa', o jeito correto de acessar é:
print(bd._BaseDeDados__dados)






