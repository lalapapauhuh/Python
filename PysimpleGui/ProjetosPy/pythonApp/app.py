#importar bibliotecas
import PySimpleGUI as sg
from faker import Faker

import os
tema = 'Reddit'
sg.theme(tema)
# Layout da aplicação 

menuzinho_def = [
['Arquivo',['Novo', 'Abrir', 'Salvar','Sair']],
    ['Editar',['Tema',['Dark','Light','Black'],'Codigo']],
    ['Ajuda','Sobre']]


layout = [
    [sg.Menu (menuzinho_def)],
    [sg.Button('Gerar Nome',size=(20,0)), 
    sg.Input(key='nome',size=(60,0))],
    [sg.Button('Gerar Profissão',size=(20,0)), sg.Input(key='profissao',size=(60,0))],
    [sg.Button('Gerar Endereço',size=(20,0)), sg.Input(key='endereco',size=(60,0))],
    [sg.Button('Gerar Placa',size=(20,0)), sg.Input(key='placa',size=(60,0))],
    [sg.Button('Gerar Cartão de Crédito',size=(20,0)), sg.Input(key='cartao_credito',size=(60,0))],

    [sg.Output(size=(85,20))],
    [sg.Button('Imprimir perfil completo'),sg.
    Button('Salvar perfil em arquivo')]
]
# Criar a janela, usando layout definido
janela = sg.Window('Faker - Gerador de dados para teste',layout=layout)
# Lendo eventos da tela, e gerar os dados
fake = Faker('pt_Br')
Faker.seed(0)

while True:
    event, valores = janela.Read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    elif event == 'Gerar Nome':
        janela['nome'].update(fake.name())
    elif event == 'Gerar Profissão':
        janela['profissao'].update(fake.job())
    elif event == 'Gerar Endereço':
        janela['endereco'].update(fake.address())
    elif event == 'Gerar Placa':
        janela['placa'].update(fake.license_plate())
    elif event == 'Gerar Cartão de Crédito':
        janela['cartao_credito'].update(fake.credit_card_full())
    elif event == 'Sobre':
        janela.disappear()
        sg.popup('Gerador de Dados fake. Versão 1.5\n 23/12/2020')
    elif event == 'Imprimir perfil completo':
        print(f'NOME: {fake.name()}{os.linesep}PROFISSÃO: {fake.job()}{os.linesep}ENDEREÇO: {fake.address()}{os.linesep}{os.linesep}PLACA: {fake.license_plate()}{os.linesep}CARTÃO: {fake.credit_card_full()}{os.linesep}')
    elif event == 'Salvar perfil em arquivo':
        with open('dados_de_teste.txt', 'a', encoding='utf-8', newline='') as arquivo:
            arquivo.write(f'NOME: {fake.name()}{os.linesep}PROFISSÃO: {fake.job()}{os.linesep}ENDEREÇO: {fake.address()}{os.linesep}PLACA: {fake.license_plate()}{os.linesep}CARTÃO: {fake.credit_card_full()}{os.linesep}')
