#Trabajo de Semana TEC

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

def line(start, end):
    "Draw line from start to end."
    up()
   #Levantar pluma
    goto(start.x, start.y)  #Inicio de la pluma Son duplas, guara dos variables
    #Bajar pluma
    down()
    goto(end.x, end.y)  #Final de la Pluma

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):  #4 veces, hace una línea y rota 90 grados
        forward(end.x - start.x)
        left(90)    #Rota a la izquierda

    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    pass  # TODO

def rectangle(start, end):
    "Draw rectangle from start to end."
    pass  # TODO

def triangle(start, end):
    "Draw triangle from start to end."
    pass  # TODO

#Recibe x y y "donde damos click"
def tap(x, y):    #Se define una variable donde se guarden coordenadas y las figuras
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)   #Donde guarda el punto 1
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line} #Dicccionario  (Desde donde se inicia)
setup(420, 420, 370, 0) 
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
