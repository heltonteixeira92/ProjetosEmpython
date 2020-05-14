# projeto 2 - Simulador de dado com interface
# Simular o uso de um dado, gerando um valor de 1 até 6

import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 0
        self.valor_maximo = 6
        self.mensagem = 'você gostaria de gerar um novo valor para o dado? '
        #layout
        self.layout = [
            [sg.Text('Jogar o Dado?')],
            [sg.Button('sim'), sg.Button('não')]
        ]
        

    
    def Iniciar(self):
        #janela
        self.janela = sg.Window('Simulador de Dado',layout = self.layout)
        #ler valores da tela
        self.eventos, self.valores = self.janela.Read()
        #fazer algo com os valores              
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Obrigado por brincar')
            else:
                print('favor digitar sim ou não')
        except:
            print('Ocorreu um erro, resposta inválida')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

Simulador = SimuladorDeDado()
Simulador.Iniciar()