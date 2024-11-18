from turtle import *

# 방향표 모양 터틀 모양으로 설정
shape("turtle")

for i in range(4):
    forward(200)
    left(90)

color("blue")
for i in range(4):
    forward(150)
    left(90)

color("red")
for i in range(4):
    forward(100)
    left(90)

color("yellow")
for i in range(4):
    forward(50)
    left(90)

# 프로세스 종료 아님
done()