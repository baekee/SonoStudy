# 전역변수
x = 10

def printx() :
    print(x)

def e_is_10():
    # 전역변수
    global e
    e = 20
    print('e 값은 ', e, '입니다')

    e = 10
    print('e 값은 ', e, '입니다')

if __name__ == '__main__' :
    printx()
    print(x)

    e_is_10()
    print(e)
