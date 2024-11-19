
# 여러 개의 수를 입력받아서 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 반환하는 프로그램을 작성하세요.
# (단, 입력은 두 개 이상의 정수라고 가정하며, 0으로 나누는 경우 등에 관한 오류를 고려할 필요는 없습니다.)\

def Four_basic_operations(num) :
    from functools import reduce

    # 문자열을 공백 기준으로 나누어 리스트에 인자 추가
    L = num.split(' ')
    # 리스트 인자 값을 내림차순 정렬
    sort_L = sorted([int(x) for x in L], reverse=True)
    # 튜플 초기화
    result = ()
    # 변수 초기화
    plus = 0
    minus = 0
    multiplication = 0
    division = 0

    # 덧셈
    plus = reduce(lambda a, b: a + b, sort_L)
    # 뺄셈
    minus = reduce(lambda a, b: a - b, sort_L)
    # 곱셈
    multiplication = reduce(lambda a, b: a * b, sort_L)
    # 나눗셈
    division = reduce(lambda a, b: a / b, sort_L)

    # 결과값 튜플 저장
    result = (plus, minus, multiplication, division)

    # 반환
    return result

# 메인 함수 호출
if __name__ == '__main__' :
    # 입력값
    num = input("두 개 이상의 정수를 공백 기준으로 입력해주세요. 예) 10 20 \n 입력 : ")
    # 변수에 결과값 저장
    result = Four_basic_operations(num)
    # 출력
    print(f"덧셈값 : {result[0]}, 뺄셈값 : {result[1]}, 곱셈값 : {result[2]}, 나눗셈값 : {result[3]}")