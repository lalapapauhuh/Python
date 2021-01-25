import ListaEndereços
from ListaEndereços import EnderecoUniversal
from ListaEndereços import EnderecoBr
from ListaEndereços import EnderecoIrlanda

lista_enderecos = [EnderecoBr('Cássio', 'São Paulo', 'NovaCidade', '0800777-7000', 'Rua: Nova', '137'),
     EnderecoIrlanda("Alfi Jones", "A26F4G9"),
     EnderecoIrlanda("Jhonson", "CB200F3")]

for item in lista_enderecos:
    if item.estaNaCidade('NovaCidade'):
        item.display()