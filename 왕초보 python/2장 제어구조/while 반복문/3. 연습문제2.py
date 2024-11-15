# 정수를 한 개 입력받아, 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트하는 프로그램을
# 작성해 보세요. 단, while 문을 사용하세요.

# from math import sqrt
print("숫자를 입력해주세요! \n" + "입력 : ")
num = int(input())
i = 0
while i < num:
    i += 1
    # print(str(i) + " " + str(i**2))
    print(i, i*i)