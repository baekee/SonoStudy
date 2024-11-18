def f1(x):
    a = 3
    b = 5
    y = a * x + b
    return y

c = f1(10)
print(c)


def f2(x):
    a = 3
    b = 5
    y = a * x + b
    print(y)

d = f2(10)
print(d)


# 삼각형의 넓이을 구하는 1. 함수
def triangle(a, b) :
    V = a * b
    return V

height = int(input("삼각형의 높이를 입력하시오. \n" + "입력 : "))
length = int(input("삼각형의 밑변의 길이를 입력하시오. \n" + "입력 : "))
V = triangle(height, length)
print(V)


# 참과 거짓
print(1 + 1 == 2)
print(1 + 1 == 3)

if 1 + 1 == 2 :
    print('yes')
else :
    print('no')

def quiz() :
    ans = input('1 + 2 = ')
    return 1 + 2 == int(ans)

print(quiz())
print(quiz())