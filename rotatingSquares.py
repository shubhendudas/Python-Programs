import turtle

lily = turtle.Turtle()
lily.speed(0)
lily.color("orange")
lily.pensize(2)

for j in range(35):
      for i in range(4):
            lily.forward(j*7)
            lily.left(90)
      lily.left(360/30)
