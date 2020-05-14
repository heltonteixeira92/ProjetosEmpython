# Projeto 1 - Simulador de dado sem interface
# Simular o uso de um dado, gerando um valor de 1 até 6

import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'você gostaria de gerar um novo valor para o dado? '
    
    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDoDado()
            elif resposta == 'não' or resposta == 'n':
                print('Obrigado por brincar')
            else:
                print('favor digitar sim ou não')
        except:
            print('Ocorreu um erro, resposta inválida')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

Simulador = SimuladorDeDado()
Simulador.Iniciar()