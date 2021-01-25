import tkinter as tk
from tkinter import ttk

def minha_funcao():
    print('A função foi chamada')
tela = tk.Tk()

my_button = tk.Button(tela, text='Exemplo', command=minha_funcao)

tela.mainloop()
