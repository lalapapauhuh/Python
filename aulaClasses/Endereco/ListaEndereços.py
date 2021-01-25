class EnderecoUniversal:
    def __init__(self, pais, destinatario):
        self.pais = pais
        self.destinatario = destinatario

    def display(self):
        print(self.destinatario)
        print(self.pais)

    def verificar(self):
        return self.destinatario != '' and self.pais != ''

    def estaNaCidade(self, cidade):
        return False
    

class EnderecoBr(EnderecoUniversal):
    def __init__(self, destinatario, estado, cidade, cep, rua, numero):
        super().__init__('Brasil', destinatario)
        self.estado = estado
        self.cidade = cidade
        self.cep = cep
        self.rua = rua
        self.numero = numero
    
    def display(self):
        print(self.destinatario)
        print(self.pais)
        print(f'{self.estado}, {self.cidade}, {self.cep}')
        print(f'{self.rua}, {self.numero}')
    
    def verificar(self):
        return (super().verificar() and self.cidade != '' and
            len(self.estado) == 2 and
            (len(self.cep) >= 8))

    def estaNaCidade(self, cidade):
        return self.cidade == cidade


class EnderecoIrlanda(EnderecoUniversal):
    def __init__(self, destinatario, cep):
        super().__init__('Irlanda', destinatario)
        self.cep = cep

    def display(self):
        print(self.destinatario)
        print(self.cep)
        print(self.pais)

    def verificar(self):
        return super().verificar() and len(self.cep) == 7
