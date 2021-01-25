import tkinter as tk
from tkinter import filedialog
import os

tela = tk.Tk()

# Cria uma lista de tuplas para cada TIPO de arquivo
meus_arquivos = [('Todos arquivos', '.*'), ('Arquivos de Texto', '.txt')]

# Pede para o usuario selecionar uma pasta
pasta = filedialog.askdirectory(parent=tela, initialdir=os.getcwd(), title='Selecione a pasta')

# Pede para o usuario selecionar um arquivo
arq = filedialog.askopenfilename(parent=tela, initialdir=os.getcwd(),
                                 title='Selecione um arquivo', filetypes=meus_arquivos)

# Pergunta se o usuario quer selecionar mais arquivos
arq2 = filedialog.askopenfilenames(parent=tela, initialdir=os.getcwd(),
                                   title='Selecione mais arquivos', filetypes=meus_arquivos)

# Pede ao usuario um nome para salvar
name_arq = filedialog.asksaveasfilename(parent=tela, initialdir=os.getcwd(),
                                        title='Nome do arquivo', filetypes=meus_arquivos)