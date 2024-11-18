# turtle로 for반복문 활용하기
from turtle import *

#color(선색깔, 채움색깔)
color('red', 'yellow')

# 채우기 시작
begin_fill()
while True :
    forward(200)
    left(170)
    if abs(pos()) < 1 :
        break
# 채우기 끝
end_fill()


# 방향표(터틀) 보여주기
showturtle()

# 방향표(터틀) 숨기기
hideturtle()

# 방향표(터틀) 보이는 여부
# showturtle() 이후는 True
# hideturtle() 이후는 False
isvisible()

done()