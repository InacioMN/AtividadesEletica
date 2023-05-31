import tkinter as tk
import math

calculo = ""

def inserir_texto(x):
    global calculo
    calculo = calculo + x
    texto.delete(1.0, "end")
    texto.insert(1.0, calculo)

def avaliar():
    global calculo
    a = str(eval(texto.get(1.0, "end")))
    calculo = ""
    inserir_texto(a)

def apagar():
    global calculo
    calculo = ""
    texto.delete(1.0, "end")

def calcular_potencia():
    global calculo
    calculo = calculo + "**"
    texto.delete(1.0, "end")
    texto.insert(1.0, calculo)

def calcular_raiz():
    global calculo
    calculo = "math.sqrt(" + calculo + ")"
    avaliar()

def calcular_inverso():
    global calculo
    calculo = "1/(" + calculo + ")"
    avaliar()

janela = tk.Tk()
texto = tk.Text(janela, height=4, width=26, font=("Arial", 24))
texto.grid(columnspan=5)

botao1 = tk.Button(janela, text="1", command=lambda: inserir_texto("1"), width=13, height=4, font=("Arial", 12))
botao1.grid(column=1, row=2)
# Resto dos botões numericos

botao_potencia = tk.Button(janela, text="^", command=calcular_potencia, width=13, height=4, font=("Arial", 12))
botao_potencia.grid(column=4, row=2)
botao_raiz = tk.Button(janela, text="√", command=calcular_raiz, width=13, height=4, font=("Arial", 12))
botao_raiz.grid(column=4, row=3)
botao_inverso = tk.Button(janela, text="1/x", command=calcular_inverso, width=13, height=4, font=("Arial", 12))
botao_inverso.grid(column=4, row=4)
# Resto dos botões de operações

botao_igual = tk.Button(janela, text="=", command=avaliar, width=27, height=4, font=("Arial", 12))
botao_igual.grid(column=1, row=6, columnspan=2)
botao_C = tk.Button(janela, text="C", command=apagar, width=27, height=4, font=("Arial", 12))
botao_C.grid(column=3, row=6, columnspan=2)

janela.mainloop()
