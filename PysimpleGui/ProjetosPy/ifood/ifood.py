import PySimpleGUI as sg
# Criar as janelas e layout
def janela_login():
    sg.theme('Dark Grey 12')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)

def janela_pedido():
    sg.theme('Dark Grey 12')
    layout = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza',key='pizza'), sg.Checkbox('Hambúrguer',key='burg')],
        [sg.Button('Fazer Pedido'), sg.Button('Voltar')]
    ]
    return sg.Window('Montar Pedido', layout=layout, finalize=True)
# Criar as janelas inciais
janela1, janela2 = janela_login(), None
# Criar um loop de leitura de eventos
while True:
    window, evento, valores = sg.read_all_windows()
    # Quando a janela for fechada
    if window == janela1 and evento == sg.WIN_CLOSED:
        break
    # Quando queremos ir para proxima janela
    if window == janela1 and evento == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and evento == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and evento == 'Fazer Pedido':
        if valores['pizza'] == True and valores['burg'] == True:
            sg.popup('Foram solicitados uma Pizza e um Hambúrguer')
        elif valores['pizza'] == True:
            sg.popup('Foi solicitado uma Pizza')
        elif valores['burg'] == True:
            sg.popup('Foi solicitado um Hambúrguer')
    # Quando queremos voltar para janela anterior
    
# logica de cada botao
