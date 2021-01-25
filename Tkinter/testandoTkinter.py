import tkinter as tk
from tkinter import *

def clicou():
    res = 'Bem-vindo ao ' + txt.get()
    msg.configure(text=res)

window = Tk()
window.title('Bem-vindo')
window.geometry('350x200')

msg = Label(window, text='Olá testando', font=('Futuras', 20))
msg.grid(row=0, column=0)

txt = Entry(window, width=30)
txt.focus()
txt.grid(row=1, column=0)


botao = Button(window, text='Clique Aqui', bg='Blue', fg='White', command=clicou)

botao.grid(row=1, column=2)

window.mainloop()