# Nessa versão há uma segunda janela, onde a expressão a ser calculada é mostrada
# Futuras melhorias: Ao clicar em '=' a expressão não é deletada / Mudar tema
import PySimpleGUI as sg
from time import sleep

# Tema
sg.theme('Reddit')
fonte_cor = 'White'
back_cor = '#0079d3'

# Tamanho da tela
WIN_W = 50
WIN_H = 100

# Menu
menu_layout = [['Arquivo', ['Novo', 'Sair']],
              ['Temas'],
              ['Ajuda', ['Sobre']]
]

layout = [
    [sg.Menu(menu_layout)],
    [sg.Input(size=(15,10), font=('Futura', 18), text_color=fonte_cor, background_color=back_cor, key='calc')],
    [sg.Input('0', size=(15,10), font=('Futura', 18), text_color=fonte_cor, background_color=back_cor, key='-BOX-')],        
    [sg.B(' C ', font=('Futura', 20), size=(2,0), key='-APAGAR-'),
     sg.B('⌫', font=('Futura', 20), size=(2,0), key='-BACKSPACE-'),
     sg.B(' x² ', font=('Futura', 20), size=(2,0), key='-QUADRADO-'),
     sg.B(' / ', font=('Futura', 20), size=(2,0), key='-DIVIDE-')],

    [sg.B(' 7 ', font=('Futura', 20), size=(2,0), key='-SETE-'),
     sg.B(' 8 ', font=('Futura', 20), size=(2,0), key='-OITO-'),
     sg.B(' 9 ', font=('Futura', 20), size=(2,0), key='-NOVE-'),
     sg.B(' * ', font=('Futura', 20), size=(2,0), key='-VEZES-')],

    [sg.B(' 4 ', font=('Futura', 20), size=(2,0), key='-QUATRO-'),
     sg.B(' 5 ', font=('Futura', 20), size=(2,0), key='-CINCO-'),
     sg.B(' 6 ', font=('Futura', 20), size=(2,0), key='-SEIS-'),
     sg.B(' - ', font=('Futura', 20), size=(2,0), key='-MENOS-')],

    [sg.B(' 1 ', font=('Futura', 20), size=(2,0), key='-UM-'),
     sg.B(' 2 ', font=('Futura', 20), size=(2,0), key='-DOIS-'),
     sg.B(' 3 ', font=('Futura', 20), size=(2,0), key='-TRES-'),
     sg.B(' + ', font=('Futura', 20), size=(2,0), key='-MAIS-')],

    [sg.B(' . ', font=('Futura', 20), size=(2,0), key='-PONTO-'),
     sg.B(' 0 ', font=('Futura', 20), size=(2,0), key='-ZERO-'),
     sg.B(' , ', font=('Futura', 20), size=(2,0), key='-VIRGULA-'),
     sg.B(' = ', font=('Futura', 20), size=(2,0), key='-IGUAL-')],
]

class App():
    def __init__(self):
        self.window = sg.Window('Calculadora Python', layout, margins=(1,1), return_keyboard_events=False)
        self.resultado = 0
        self.operador = ''
        self.window.read(timeout=5)
    
    # Funções do Menu
    def sobre_menu(self):
        sg.popup('Sobre', 'Minha calculadora versão 1.1', 'CASSIO645')
    
    # Função dos resultados
    def resultado_calc(self):
        if self.operador == '+':
            return float(self.resultado) + float(self.values['-BOX-'])
        if self.operador == '-':
            return float(self.resultado) - float(self.values['-BOX-'])
        if self.operador == '*':
            return float(self.resultado) * float(self.values['-BOX-'])
        if self.operador == '/':
            return float(self.resultado) / float(self.values['-BOX-'])
        if self.operador == 'x²':
            return float(self.resultado) * float(self.resultado)

    # Função que mantem rodando
    def start(self):
        while True:
            event, self.values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Sair':
                break
            if event in ('Sobre'):
                self.sobre_menu()

            if event in ('-UM-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='1')
                    self.window['calc']('1')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '1')
                    self.window['calc'].update(value=self.values['calc'] + '1')

            if event in ('-DOIS-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='2')
                    self.window['calc']('2')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '2')
                    self.window['calc'].update(value=self.values['calc'] + '2')

            if event in ('-TRES-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='3')
                    self.window['calc']('3')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '3')
                    self.window['calc'].update(value=self.values['calc'] + '3')

            if event in ('-QUATRO-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='4')
                    self.window['calc']('4')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '4')
                    self.window['calc'].update(value=self.values['calc'] + '4')

            if event in ('-CINCO-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='5')
                    self.window['calc']('5')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '5')
                    self.window['calc'].update(value=self.values['calc'] + '5')

            if event in ('-SEIS-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='6')
                    self.window['calc']('6')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '6')
                    self.window['calc'].update(value=self.values['calc'] + '6')

            if event in ('-SETE-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='7')
                    self.window['calc']('7')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '7')
                    self.window['calc'].update(value=self.values['calc'] + '7')


            if event in ('-OITO-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='8')
                    self.window['calc']('8')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '8')
                    self.window['calc'].update(value=self.values['calc'] + '8')

            if event in ('-NOVE-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='9')
                    self.window['calc']('9')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '9')
                    self.window['calc'].update(value=self.values['calc'] + '9')

            if event in ('-ZERO-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='0')
                    self.window['calc']('0')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '0')
                    self.window['calc'].update(value=self.values['calc'] + '0')
            
            if event in ('-PONTO-'):
                if self.values['-BOX-'] == '0' or self.values['-BOX-'] == ',':
                    pass
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '.')
                    self.window['calc'].update(value=self.values['calc'] + '.')

            if event in ('-VIRGULA-'):
                if self.values['-BOX-'] == '0' or self.values['-BOX-'] == '.':
                    pass
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + ',')
                    self.window['calc'].update(value=self.values['calc'] + ',')

            # Funções especiais, apagar ultimo e apagar tudo
            if event in ('-APAGAR-'):
                self.resultado = 0
                self.window['-BOX-'].update(value=self.resultado)
                self.window['calc'].update('')

            if event in ('-BACKSPACE-'):
                self.window['-BOX-'].update(value=self.values['-BOX-'][:-1])
                self.window['calc'].update(value=self.values['calc'][:-1])

            # Funções + - * / x²
            if event in ('-MAIS-'):
                if self.operador != '':
                    self.resultado = self.resultado_calc()
                else:
                    self.operador = '+'
                    self.resultado = self.values['-BOX-']
                self.window['calc'].update(value=self.values['calc'] + '+')
                self.window['-BOX-'].update(value='')


            if event in ('-MENOS-'):
                if self.operador != '':
                    self.resultado = self.resultado_calc()
                else:
                    self.operador = '-'
                    self.resultado = self.values['-BOX-']
                self.window['calc'].update(value=self.values['calc'] + '-')
                self.window['-BOX-'].update(value='')

            if event in ('-DIVIDE-'):
                if self.operador != '':
                    self.resultado = self.resultado_calc()
                else:
                    self.operador = '/'
                    self.resultado = self.values['-BOX-']
                self.window['calc'].update(value=self.values['calc'] + '/')
                self.window['-BOX-'].update(value='')

            if event in ('-VEZES-'):
                if self.operador != '':
                    self.resultado = self.resultado_calc()
                else:
                    self.operador = '*'
                    self.resultado = self.values['-BOX-']
                self.window['calc'].update(value=self.values['calc'] + '*')
                self.window['-BOX-'].update(value='')
            
            if event in ('-QUADRADO-'):
                if self.operador != '':
                    self.resultado = self.resultado_calc()
                else:
                    self.operador = 'x²'
                    self.resultado = self.values['-BOX-']
                self.resultado = self.resultado_calc()
                self.window['calc'].update(value=self.values['calc'] + '²')
                self.window['-BOX-'].update(value=self.resultado)
                self.resultado = 0
                self.operador = ''

            if event in ('-IGUAL-'):
                self.resultado = self.resultado_calc()
                self.window['calc'].update('')
                self.window['-BOX-'].update(value=self.resultado)
                self.resultado = 0
                self.operador = ''
            
                

App().start()