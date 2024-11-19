# 두 수를 입력받아서 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 반환하는 프로그램을 작성하세요.
# (단, 입력은 정수로 가정하며, 0으로 나누는 경우 등에 관한 오류를 고려할 필요는 없습니다.

def Four_basic_operations(num) :
    # 입력받은 수 공백제거 및 , 기준으로 나누기
    num = list(map(int, num.replace(' ', '').split(',')))
    # 변수 정의
    # a = num[0]
    # b = num[1]
    a, b = (num[0], num[1])
    result = [a + b, a - b, a * b, a / b]

    return result

if __name__ == '__main__' :
    num = input("두 수를 입력해 주세요. \n 두 수의 구분은 , 로 합니다. 예)10, 20 \n 입력 : ")
    result = Four_basic_operations(num)
    print(f'덧셈값 : {result[0]}, 뺄셈값 : {result[1]}, 곱셈값 : {result[2]}, 나눗셈값 : {result[3]}')