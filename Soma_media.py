#programa para pedir notas e somar a média com GUI
import PySimpleGUI as sg

class SomaMedia:
    def __init__(self):
        self.nota_one = 'nota_one'
        self.nota_two = 'nota_two'
        self.nota_three = 'nota_three'
        self.media = 0
        #layout
        self.layout = [
            [sg.Text('Nota Av1:'),sg.Input(key='nota_one')],
            [sg.Text('Nota Av2:'),sg.Input(key='nota_two')],
            [sg.Text('Nota Av3:'),sg.Input(key='nota_three')],
            [sg.Button('OK')],
            [sg.Output(size=(20,10))]
         ]
    def Inicio(self):
        #janela
        self.janela = sg.Window('Soma média',layout = self.layout)
        #ler valores na tela
        self.valores, self.eventos = self.janela.Read()
        #fazer algo com valores   
        self.Calculo()         
        try:
            while True:
                if self.evento == 'OK':                    
                    if int(self.media) >= 6 and int(self.media) <10:
                        print('You are ok, good')
                    elif int(self.media) == 10:
                        print('Congrulations, you are a good student')
                    elif int(self.media) < 6:
                        print("You are bad, don't cry")
        except:
            print('Algo deu errado')

       
    def Calculo(self):
        self.media = (int(self.nota_one) + int(self.nota_three)+ int(self.nota_two)) / 3
        print(f'A soma das notas {self.nota_one}, {self.nota_two}, {self.nota_three} / 3 = {self.media}')
    
Media = SomaMedia()
Media.Inicio()