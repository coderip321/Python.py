from turtle import*
import colorsys
speed(90)
hideturtle()
bgcolor("black")
tracer(5)
width(2)
h=0.01
for i in range(55):
      color(colorsys.hsv_to_rgb(h,1,1))
      forward(100)
      left(60)
      forward(100)
      right(120)
      circle(50)
      left(240)
      forward(100)
      left(60)
      forward(100)
      h+=0.02
      color(colorsys.hsv_to_rgb(h,1,1))
      forward(100)
      left(60)
      forward(100)
      right(120)
      circle(-50)
      left(240)
      forward(100)
      left(60)
      forward(100)
      left(2)
      h+=0.02
done()