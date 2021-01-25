import tkinter as tk
from tkinter import simpledialog
from tkinter import colorchooser


tela = tk.Tk()


#caixa de cores igual paint
rgb_color, web_color = colorchooser.askcolor(parent=tela, initialcolor= (255, 0, 0))


nome = simpledialog.askstring("Input", "Digite seu nome ", parent=tela)
if nome is not None:
    print('Seu nome é', nome)  
else:
    print('Você não digitou seu nome!!')


idade = simpledialog.askinteger('Input', 'Digite sua idade', parent=tela, minvalue=0, maxvalue=100)
if idade is not None:
    print(f'Você tem {idade} anos') 
else:
    print('Você não digitou nada!')


altura = simpledialog.askfloat('Input', 'Digite sua altura', parent=tela, minvalue=0.5, maxvalue=2.5)
if altura is not None:
    print(f'Você mede {altura}m')
else:

    print('Você não informou sua altura!!')

