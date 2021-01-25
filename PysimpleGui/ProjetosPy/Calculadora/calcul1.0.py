import PySimpleGUI as sg

sg.theme('Reddit')

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
    [sg.Input('0', size=(15,10), font=('Futura', 18), text_color='White', background_color='#0079d3', key='-BOX-')],        
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
        self.window.read(timeout=1)
    
    # Funções do Menu
    def sobre_menu(self):
        sg.popup('Sobre', 'Minha calculadora 29/12/2020', 'CASSIO645')
    
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
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '1')

            if event in ('-DOIS-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='2')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '2')

            if event in ('-TRES-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='3')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '3')

            if event in ('-QUATRO-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='4')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '4')

            if event in ('-CINCO-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='5')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '5')

            if event in ('-SEIS-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='6')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '6')

            if event in ('-SETE-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='7')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '7')


            if event in ('-OITO-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='8')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '8')

            if event in ('-NOVE-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='9')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '9')

            if event in ('-ZERO-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='0')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '0')
            
            if event in ('-PONTO-'):
                if self.values['-BOX-'] == '0' or self.values['-BOX-'] == ',':
                    pass
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '.')

            if event in ('-VIRGULA-'):
                if self.values['-BOX-'] == '0' or self.values['-BOX-'] == '.':
                    pass
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + ',')

            # Funções especiais, apagar ultimo e clear all
            if event in ('-APAGAR-'):
                self.resultado = 0
                self.window['-BOX-'].update(value=self.resultado)

            if event in ('-BACKSPACE-'):
                self.window['-BOX-'].update(value=self.values['-BOX-'][:-1])

            # Funções + - * / x²
            if event in ('-MAIS-'):
                if self.operador != '':
                    self.resultado = self.resultado_calc()
                else:
                    self.operador = '+'
                    self.resultado = self.values['-BOX-']
                self.window['-BOX-'].update(value='')

            if event in ('-MENOS-'):
                if self.operador != '':
                    self.resultado = self.resultado_calc()
                else:
                    self.operador = '-'
                    self.resultado = self.values['-BOX-']
                self.window['-BOX-'].update(value='')

            if event in ('-DIVIDE-'):
                if self.operador != '':
                    self.resultado = self.resultado_calc()
                else:
                    self.operador = '/'
                    self.resultado = self.values['-BOX-']
                self.window['-BOX-'].update(value='')

            if event in ('-VEZES-'):
                if self.operador != '':
                    self.resultado = self.resultado_calc()
                else:
                    self.operador = '*'
                    self.resultado = self.values['-BOX-']
                self.window['-BOX-'].update(value='')
            
            if event in ('-QUADRADO-'):
                if self.operador != '':
                    self.resultado = self.resultado_calc()
                else:
                    self.operador = 'x²'
                    self.resultado = self.values['-BOX-']
                self.resultado = self.resultado_calc()
                self.window['-BOX-'].update(value=self.resultado)
                self.resultado = 0
                self.operador = ''

            if event in ('-IGUAL-'):
                self.resultado = self.resultado_calc()
                self.window['-BOX-'].update(value=self.resultado)
                self.resultado = 0
                self.operador = ''

App().start()