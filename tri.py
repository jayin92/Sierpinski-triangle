# import package
import turtle
import random
import math
random.seed()
# 定義三角形三頂點
pointa = (0,400)
pointb = (-650,-300)
pointc = (650,-300)
point = [pointa, pointb, pointc] 
# 定義第一個點(若這個點為隨機產出一樣對產出三角形完全沒有影響)
firstpoint = (-200,250)

# 定義繪點函數(傳入tuple)
def drawdot(point, color='black'):
	turtle.penup()
	turtle.goto(point[0],point[1])
	turtle.pendown()
	turtle.dot(2, color)
# 傳入兩個點(tuple)回傳兩點中點座標(tuple)
def gohalf(point1,point2):
	point = ((point1[0] + point2[0]) / 2, ((point1[1] + point2[1]) / 2))	
	return point
# turtle package init
turtle.speed(0)
turtle.delay(0)
turtle.hideturtle()
# 開始繪圖
drawdot(pointa)
drawdot(pointb)
drawdot(pointc)
drawdot(firstpoint, 'green')
# 將追蹤點定義為起始點
tracepoint = firstpoint
i = 1
#進入無限迴圈
while True:
	print(i)
	# 從point(list)隨機拿出任一個三角形頂點
	random_point = random.choice(point)
	# 產出中點座標
	gopoint = gohalf(tracepoint, random_point)
	# 描點
	drawdot(gopoint)
	# 將追蹤點定義為新產出的中點
	tracepoint = gopoint
	i += 1
turtle.exitonclick()