#Trabajo de Semana TEC

#Código modificado por:

#Autor: Ricardo Rmz. Condado
#Autor: Nancy L. Garcia Jimenez

"""Paint, for drawing shapes.
Exercises
1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
from freegames import vector

#Define cómo es que funciona la línea

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

#Establece como se dibujará un cuadrado
#Con base a un ciclo es como se dibuja.
#Cuando dibuje una línea, dará una vuelta a 90°

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)
    end_fill()

#Se le colocó el nombre "circlee"
#Después se usó "circle" para dibujar

def circlee(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    bgcolor("blue")
    color("black", "red")
    down()
    begin_fill()

    circle((end.x - start.x)
            /2)
    end_fill()

#Se coloca un ciclo for para crear el dibujo.

def rectangle(start, end):

    up()
    goto(start.x,start.y)
    down()
    begin_fill()
    for i in range(2):
        forward(200)
        right(90)
        forward(100)
        right(90)
    end_fill()

#Dibuja el triángulo con un for.

def triangle(start, end):

    up()#línea hacia arriba
    goto(start.x,start.y)
    down()
    begin_fill()
    for i in range(2):
        forward(end.x - start.y)
        right(90)
        right(150)
    end_fill()

#Se almacenan coordenadas x, y al dar click

def tap(x, y):
    "Store starting point or draw shape."

    #Estado actual de state
    start = state['start']

#Condicional para determinar si se traza la figura o no.

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

#Almacena la figura hasta que pulsamos alguna tecla.

def store(key, value):
    "Store value in state at key."
    state[key] = value

#Guarda el primer punto, por defecto traza una línea

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')

#Define las teclas que cambian de color
#Mas aparte color nuevo

onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color ('yellow'), 'Y')

#Define la tecla asociada a cada figura

onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circlee), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
