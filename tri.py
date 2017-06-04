import turtle
import random
import math
random.seed()
pointa = (0,400)
pointb = (-650,-300)
pointc = (650,-300)
point = [pointa, pointb, pointc]
firstpoint = (-200,250)

def drawdot(point, color='black'):
	turtle.penup()
	turtle.goto(point[0],point[1])
	turtle.pendown()
	turtle.dot(2, color)
def gohalf(point1,point2):
	point = ((point1[0] + point2[0]) / 2, ((point1[1] + point2[1]) / 2))	
	return point


turtle.speed(0)
turtle.delay(0)
turtle.hideturtle()
drawdot(pointa)
drawdot(pointb)
drawdot(pointc)
drawdot(firstpoint, 'green')
tracepoint = firstpoint
i = 1
while True:
	print(i)
	random_point = random.choice(point)	
	gopoint = gohalf(tracepoint, random_point)
	drawdot(gopoint)
	tracepoint = gopoint
	i += 1
turtle.exitonclick()