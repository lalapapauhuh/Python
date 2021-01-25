import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

wn = tk.Tk()
wn.geometry('200x300')
tela = ttk.Label(wn, text='Olá Mundo')

tela.grid(row=1, column=1)

#messagebox.show(((info/warning/error)))("Informações","TA MUUUUITO HACKEADO")
#resposta = messagebox.ask((okcancel/retrycancel/yesno/yesnocancel)) ('Salvar dados cliente', 'Deseja salvar os dados? ')
resposta = messagebox.askyesnocancel ('Salvar dados cliente', 'Deseja salvar os dados? ')
print(resposta)

saida_botao = ttk.Button(tela, text='Sair')
saida_botao.grid(row=2, column=1)
saida_botao['command'] = tela.destroy

wn.mainloop()