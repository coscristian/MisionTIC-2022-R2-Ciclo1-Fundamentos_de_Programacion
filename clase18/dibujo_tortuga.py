import turtle as t
import math

t.clear()
t.shape('turtle')
t.speed(2.5)

t.color("red", "blue")

t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)
t.begin_fill()
t.left(135)

t.forward(math.sqrt((300**2) + (300**2)))
t.end_fill()
t.mainloop()