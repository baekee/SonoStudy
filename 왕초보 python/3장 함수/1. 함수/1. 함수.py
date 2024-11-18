# 1. 함수 정의 def
a_list = list(range(10))

def print_list(a) :
    for i in a:
        print(i)

print_list(a_list)

# 매개변수없는 1. 함수
def boy() :
    print("I am a boy.")
    print('You are a girl.')

boy()

# a와 b 가운데 a가 크면 'a > b'라고 표시하고, b가 크면 'a < b',
# 두 숫자가 같으면 'a == b'라고 표시하는 함수를 만들어 보세요.
# 이 함수는 매개변수 두 개를 필요로 합니다.

def equal_int(a, b) :
    if a > b :
        print('a > b')
    elif a == b :
        print('a == b')
    else :
        print('a < b')

equal_int(input("비교할 숫자를 입력해주세요. \n" + "입력 : "), input("비교할 숫자를 입력해주세요. \n" + "입력 : "))