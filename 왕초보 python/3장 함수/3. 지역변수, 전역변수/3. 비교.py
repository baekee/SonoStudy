# 전역변수
x = 10

def x_is_20():
    # 지역변수
    x = 20
    print("지역 변수의 메모리 주소 값 : ",id(x))
    print('x 값은 ', x, '입니다')

def x_is_50() :
    global x
    x = 50
    print("지역 변수의 메모리 주소 값 : ", id(x))
    print('x 값은 ', x, '입니다')


if __name__ == '__main__' :
    x_is_20()
    print("전역 변수의 메모리 주소 값 : ", id(x))
    print(x)
    x_is_50()
    print("전역 변수의 메모리 주소 값 : ", id(x))
    print(x)