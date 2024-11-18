# 정삼각형, 정사각형 및 다각형 그리는 1. 함수 활용

from turtle import *
shape('turtle')
goto(200, -200)

# 정삼각형
def triangle(side) :
    for i in range(3) :
        forward(side)
        left(120)

color('red')
triangle(200)

goto(50, -200)

# 정사각형
def rectangle(side) :
    for i in range(4):
        forward(side)
        left(90)

rectangle(100)
color('blue')
rectangle(150)

# 다각형
def polygon(side, n) :
    for i in range(n) :
        forward(side)
        left(180 - ((n-2)*180/n))

goto(-300, -300)
polygon(100, 3)
goto(-300, -200)
polygon(100, 4)
goto(-300, -50)
polygon(100, 5)
goto(-300, 150)
polygon(100, 6)

done()