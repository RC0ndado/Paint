# Paint
Actividad 1. Juego Pintando SEMANA TEC

El código mostraba un juego en el que se dibujaban figuras dependiendo: líneas, circulos, triangulos, cuadrados y rectángulos (solo si se apretaba la tecla a la que pertenezca la figura).
Para que se pudiera dibujar la figura, se tenían que dar click a dos puntos del campo para que empezara a dibujar la figura.

Las modificaciones que se solicitaron en el juego fueron: 

* Agregar un nuevo color en el código
* Escribir las intrucciones necesarias para que dibujara un círculo, un triángulo, o un rectángulo.



## Ricardo:
1. Para agregar un nuevo color sólo se agregó una nueva línea de texto en la fila 127 para colocar "onkey(lambda: color ('yellow'), 'Y')"
2. Para la realización del círculo solo se cambió el nombre de la función original "circle" porque al crear la nueva función y al realizarle algunas modificaciones, como lo fue hacer (end.x - start.x)/2, llamaría a la función "circle" y diburía el círculo totalmente.


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


## Nancy
3. Coloqué un ciclo for para que en base a los dos puntos dados, se trazara la figura, en el caso del rectángulo se dió un giro de 90°
4. Coloqué un ciclo for para que en base a los dos puntos dados, se trazara la figura, en el caso del triángulo se realizó una resta de puntos con la función forward (forward(end.x - start.y)) junto a giros de 90° y 150°.

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
  
