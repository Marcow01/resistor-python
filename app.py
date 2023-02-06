from tkinter import *

root = Tk()
root.title("Resistor.app")
root.geometry("500x300")
root.minsize(500,300)
root.maxsize(600,400)

contagem = 0;
coreshex = ['#000000', '#7f4f24', '#c1121f', '#f77f00', '#ffd60a', '#8ac926', '#1982c4', '#6a4c93', '#495057', '#dee2e6']
faixa1 = coreshex[0]

def atualizarCor():
    global coreshex
    global faixa1
    faixa1 = coreshex[int(contagem)]

    return print(faixa1)

def desenhar():
    canvas.create_rectangle(0, 0,70, 70, fill=faixa1)
    canvas.grid(row=2, column=0)
    
def somar():
    global faixa1
    global contagem
    contagem += 1

    if contagem == 10:
        contagem -= 1
    
    atualizarCor() 
    desenhar()
    return print(contagem)

def subtrair():
    global contagem
    contagem -= 1

    if contagem == -1:
        contagem += 1
    
    atualizarCor()
    desenhar()
    return print(contagem)

faixa1Soma = Button(root,
               text='Somar',
               command=somar
)

faixa1Sub = Button(root,
               text='Subtrair',
               command=subtrair
)

canvas = Canvas(root, 
           width=300,
           height=250
)

texto = Label(root, text=contagem)

#desenhar()

faixa1Soma.grid(row=0, column=0)
faixa1Sub.grid(row=1, column=0)
texto.grid(row=3, column=5)
root.mainloop()