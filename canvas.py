from tkinter import *

root = Tk()
root.title("Resistor.app")
root.geometry("870x300")
root.minsize(500,300)
root.maxsize(900,400)

faixa1Value = 2
faixa2Value = 4
faixa3Value = 7
multiplicadorValue = 3
toleranciaValue = 2
coreshex = ['#000000', '#7f4f24', '#c1121f', '#f77f00', '#ffd60a', '#8ac926', '#1982c4', '#6a4c93', '#495057', '#dee2e6']
corestolerancia = ['#7f4f24', '#c1121f',  '#ff7f51', '#6c757d', '#FFFFFF']
coresmultiplicador = ['#000000', '#7f4f24', '#c1121f', '#f77f00', '#ffd60a', '#8ac926', '#1982c4', '#6a4c93', '#495057', '#dee2e6'] 
tolerancias = [1, 2, 5, 10, 20]
multiplicadores = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 0.1, 0.01]
faixa1 = coreshex[2]
faixa2 = coreshex[4]
faixa3 = coreshex[7]
multiplicadorCor = coresmultiplicador[3]
toleranciaCor = corestolerancia[2]

def atualizarCor():
    global coreshex
    global faixa1
    global faixa2
    global faixa3
    global multiplicadorCor
    global toleranciaCor
    global tolerancias

    faixa1 = coreshex[int(faixa1Value)]
    faixa2 = coreshex[int(faixa2Value)]
    faixa3 = coreshex[int(faixa3Value)]
    multiplicadorCor = coresmultiplicador[int(multiplicadorValue)]
    toleranciaCor = corestolerancia[int(toleranciaValue)]
    resultado = int(str(faixa1Value) + str(faixa2Value) + str(faixa3Value))*multiplicadores[multiplicadorValue]
    texto = Label(root, text=f"o valor é: {resultado} ± {tolerancias[toleranciaValue]}% Ω")
    texto.grid(row=3, column=5)

def desenhar():
    canvas.create_rectangle(0, 0, 100, 100, fill=faixa1)
    canvas.create_rectangle(100, 0, 200, 100, fill=faixa2)
    canvas.create_rectangle(200, 0, 300, 100, fill=faixa3)
    canvas.create_rectangle(300, 0, 400, 100, fill=multiplicadorCor)
    canvas.create_rectangle(400, 0, 500, 100, fill=toleranciaCor)

    atualizarCor()
    
def faixa1Somar():
    global faixa1
    global faixa1Value
    faixa1Value += 1

    if faixa1Value == 10:
        faixa1Value -= 1
    
    atualizarCor() 
    desenhar()

def faixa1Sub():
    global faixa1Value
    faixa1Value -= 1

    if faixa1Value == -1:
        faixa1Value += 1
    
    atualizarCor()
    desenhar()

def faixa2Somar():

    global faixa2Value
    faixa2Value += 1

    if faixa2Value == 10:
        faixa2Value -= 1
    
    atualizarCor() 
    desenhar()

def faixa2Sub():
    global faixa2Value
    faixa2Value -= 1

    if faixa2Value == -1:
        faixa2Value += 1
    
    atualizarCor()
    desenhar()

def faixa3Somar():
    global faixa3Value
    faixa3Value += 1

    if faixa3Value == 10:
        faixa3Value -= 1
    
    atualizarCor() 
    desenhar()

def faixa3Sub():
    global faixa3Value
    faixa3Value -= 1

    if faixa3Value == -1:
        faixa3Value += 1
    
    atualizarCor()
    desenhar()

def multiplicadorSomar():
    global multiplicadorValue
    multiplicadorValue += 1

    if multiplicadorValue == 10:
        multiplicadorValue -= 1
    
    atualizarCor() 
    desenhar()

def multiplicadorSub():
    global multiplicadorValue
    multiplicadorValue -= 1

    if multiplicadorValue == -1:
        multiplicadorValue += 1
    
    atualizarCor()
    desenhar()

def toleranciaSomar():
    global toleranciaValue
    toleranciaValue += 1

    if toleranciaValue == 5:
        toleranciaValue -= 1
    
    atualizarCor() 
    desenhar()


def toleranciaSub():
    global toleranciaValue
    toleranciaValue -= 1

    if toleranciaValue == -1:
        toleranciaValue += 1
    
    atualizarCor()
    desenhar()

faixa1Soma = Button(root,
               text='Somar',
               command=faixa1Somar
)

faixa1Subtrair = Button(root,
               text='Subtrair',
               command=faixa1Sub
)

faixa2Soma = Button(root,
               text='Somar',
               command=faixa2Somar
)

faixa2Subtrair = Button(root,
               text='Subtrair',
               command=faixa2Sub
)

faixa3Soma = Button(root,
               text='Somar',
               command=faixa3Somar
)

faixa3Subtrair = Button(root,
               text='Subtrair',
               command=faixa3Sub
)

multiplicadorSoma = Button(root,
               text='Somar',
               command=multiplicadorSomar
)

multiplicadorSubtrair = Button(root,
               text='Subtrair',
               command=multiplicadorSub
)

toleranciaSoma = Button(root,
               text='Somar',
               command=toleranciaSomar
)

toleranciaSubtrair = Button(root,
               text='Subtrair',
               command=toleranciaSub
)

canvas = Canvas(root, 
           width=500,
           height=100,
           bg='#8ac926'
)




desenhar()

canvas.grid(row=3, column=0)

faixa1Soma.grid(row=0, column=0)
faixa1Subtrair.grid(row=1, column=0)

faixa2Soma.grid(row=0, column=1)
faixa2Subtrair.grid(row=1, column=1)

faixa3Soma.grid(row=0, column=2)
faixa3Subtrair.grid(row=1, column=2)

multiplicadorSoma.grid(row=0, column=3)
multiplicadorSubtrair.grid(row=1, column=3)

toleranciaSoma.grid(row=0, column=4)
toleranciaSubtrair.grid(row=1, column=4)

root.mainloop()