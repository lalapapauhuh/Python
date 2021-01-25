from tkinter import *
from tkinter.ttk import *

def evento(event):
    print('Funcionou')

janela = Tk()
janela.title('Bem-vindo ao combobox')
janela.geometry('400x250')

# ADICIONANDO Combobox
combo = Combobox(janela)
combo['values'] = (1, 2, 3, 4, 5,  "Text")
combo.current(1) # define o item selecionado
combo.grid(column=0, row=0)

# ADICIONANDO Checkbutton
checando = BooleanVar()
escolha = Checkbutton(janela, text= 'Escolha', var=checando)
escolha.grid(column=0, row=1)

# ADICIONANDO RADIO BUTTON
selected = IntVar()
rad1 = Radiobutton(janela, text='Primeiro', value=1, variable=selected)
rad2 = Radiobutton(janela, text='Segundo', value=2, variable=selected)
rad3 = Radiobutton(janela, text='Terceiro', value=3, variable=selected)

def clicado():
    print(selected.get)

botao = Button(janela, text='Enviar', command=clicado)
botao.grid(column=0, row=4)
botao.bind('<Enter>', evento)
rad1.grid(column=0, row=3)
rad2.grid(column=1, row=3)
rad3.grid(column=2, row=3)


janela.mainloop()