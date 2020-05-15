#programa para pedir notas e somar a média
import PySimpleGUI as sg

class SomaMedia:
    def __init__(self):
        self.nota_one = 0
        self.nota_two = 0
        self.nota_three = 0
        self.media = 0
        layout = [
            [sg.Text('Nota:'),sg.Input(key=self.nota_one)],
            [sg.Text('Nota:'),sg.Input(key=self.nota_two)],
            [sg.Text('Nota:'),sg.Input(key=self.nota_three)]
        ]
    def Inicio(self):
        #janela
        self.janela = sg.Window('Soma média',layout = self.layout)
        #ler valores na tela
        self.valores, self.eventos = self.janela.Read()
        #fazer algo com valores
        print('Calculadora de Média')
        print('--'* 10)
        self.PrimeiraNota()
        self.SegundaNota()
        self.TerceiraNota()
        self.Calculo()
        if self.media >= 6 and self.media <10:
            print('You are ok, good')
        elif self.media == 10:
            print('Congrulations, you are a good student')
        elif self.media < 6:
            print("You are bad, don't cry")


    def PrimeiraNota(self):
        self.nota_one = int(input('Digite a primeira nota: '))
    
    def SegundaNota(self):
        self.nota_two = int(input('Digite a segunda nota: '))

    def TerceiraNota(self):
        self.nota_three = int(input('Digite a terceira nota: '))
    
    def Calculo(self):
        self.media = (self.nota_one + self.nota_three + self.nota_two) / 3
        print(f'A soma das notas {self.nota_one}, {self.nota_two}, {self.nota_three} / 3 = {self.media}')
    
Media = SomaMedia()
Media.Inicio()