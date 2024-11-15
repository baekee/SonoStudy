# 값의 크기 비교
a = 1234 * 4
b = 13456 / 2

if a > b :
    print('a')
else :
    print('b')

# 값 비교
c = 15 * 5
d = 15 + 15 + 15 + 15 + 15
if c > d :
    print('c is greater than d')
elif c == d :
    print('c is equal to d')
elif c < d :
    print('c is less than d')
else :
    print('i don\'t know')

# 나머지 연산자
num1 = 48
num2 = 4

if num1 % num2 == 0 :
    print(f'{num1}는 {num2} 로 나누어 떨어집니다.')
elif num1 % num2 != 0 :
    print(f'{num1}는 {num2}로 나우어 떨어지지 않습니다.')

# 조건에 따라 반복문 중단하기

max = 10

while True :
    num = int(input())
    if num > max :
        print(num, 'is too big!')
        break