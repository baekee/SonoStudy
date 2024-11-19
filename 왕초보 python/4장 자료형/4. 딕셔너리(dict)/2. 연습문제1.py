# 매개변수로 입력받은 정수에 해당하는 한글 문자열을 반환하는 함수 korean_number()를 if 문을 사용하지 말고 작성하세요.
# 단 :사용자는 0 이상 9 이하의 정수 중 하나를 입력한다고 가정합니다.

def korean_number(num) :
    # 딕셔너리 정의
    tras_korea = {1 : '일', 2 : '이', 3 : '삼', 4 : '사', 5 : '오', 6 : '육', 7 : '칠', 8 : '팔', 9 : '구'}
    # 반환
    return tras_korea[num]

if __name__ == '__main__' :
    # 입력값
    num = int(input("0 이상 9 이하의 정수 중 하나를 입력하시오. \n 입력 : "))
    # 결과값
    result = korean_number(num)
    # 출력
    print(result)
