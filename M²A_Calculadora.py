from tkinter import *
from math import *

#FUNCIÓN PARA MOSTRAR NÚMEROS POR PANTALLA

def btnClick(num):
    global operador
    operador = operador + str(num)
    input_text.set(operador)

#CÁLCULO Y MUESTRA DE RESULTADOS

def resultado():
    global operador
    try:
        opera = str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set("ERROR")
    operador = ""

#FUNCIÓN PARA LIMPIAR LA PANTALLA

def clear():
    global operador
    operador=("")
    input_text.set("0")



ventana = Tk()
ventana.title("CALCULADORA")
ventana.geometry("392x600")

#DIMENSIONES DE LOS BOTONES
ancho_boton = 11
alto_boton = 3

#COLOR DE LOS BOTONES Y DEL FONDO

ventana.configure(background="SkyBlue4")
color_boton=("gray77")

#VARIABLES PARA LA FUNCION "btnClick"
input_text = StringVar()
operador = ""



Salida = Entry(ventana, font=('arial', 20, 'bold'), width=22, textvariable=input_text, bd=20, insertwidth=4, bg="powder blue", justify="right")
Salida.place(x=10, y=60)

#NUESTROS BOTONES

Boton0 = Button(ventana, text="0", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick(0)).place(x=107, y=540)
Boton1 = Button(ventana, text="1", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick(1)).place(x=17, y=480)
Boton2 = Button(ventana, text="2", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick(2)).place(x=107, y=480)
Boton3 = Button(ventana, text="3", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick(3)).place(x=197, y=480)
Boton4 = Button(ventana, text="4", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick(4)).place(x=17, y=420)
Boton5 = Button(ventana, text="5", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick(5)).place(x=107, y=420)
Boton6 = Button(ventana, text="6", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick(6)).place(x=197, y=420)
Boton7 = Button(ventana, text="7", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick(7)).place(x=17, y=360)
Boton8 = Button(ventana, text="8", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick(8)).place(x=107, y=360)
Boton9 = Button(ventana, text="9", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick(9)).place(x=197, y=360)

BotonSuma = Button(ventana, text="+", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick("+")).place(x=17, y=300)
BotonResta = Button(ventana, text="-", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick("-")).place(x=107, y=300)
BotonMultiplicacion = Button(ventana, text="x", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick("*")).place(x=197, y=300)
BotonDivision = Button(ventana, text="÷", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick("/")).place(x=287, y=300)

BotonResultado = Button(ventana, text="=", bg=color_boton, width=ancho_boton, height=alto_boton, command=resultado).place(x=287, y=540)
BotonC = Button(ventana, text="C", bg=color_boton, width=ancho_boton, height=alto_boton, command=clear).place(x=287, y=180)

BotonComa = Button(ventana, text=",", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick(",")).place(x=197, y=540)
BotonNegativo = Button(ventana, text="+/-", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick("+/-")).place(x=17, y=540)

BotonPorcentaje = Button(ventana, text="%",bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick("%")).place(x=287, y=480)
BotonPi = Button(ventana, text="π", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick("pi")).place(x=287, y=420)
BotonRaiz = Button(ventana, text="√", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick("sqrt(")).place(x=287, y=360)

BotonParen1 = Button(ventana, text="(", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick("(")).place(x=17, y=240)
BotonParen2 = Button(ventana, text=")", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick(")")).place(x=107, y=240)
BotonLn = Button(ventana, text="ln", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick("log")).place(x=197, y=240)
BotonExp = Button(ventana, text="EXP", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda:btnClick("**")).place(x=287, y=240)

clear()

ventana.mainloop()