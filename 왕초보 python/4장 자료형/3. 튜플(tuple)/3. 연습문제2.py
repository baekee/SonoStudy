# 사용자로부터 날짜를 나타내는 세 개의 숫자를 입력받습니다.
# 첫 번째 숫자는 연도를 나타내는 네 자리 숫자이고, 두 번째 숫자는 월을, 세 번째 숫자는 일을 나타냅니다.
#
# 입력받은 날짜를 mm/dd/yyyy 형식으로 출력합니다.
#
# 월을 두 자리 숫자(01, 02, 03, ..., 12)로, 일을 두 자리 숫자(01, 02, 03, ..., 31)로, 연도를 네 자리 숫자로 나타냅니다.
#
# 입력받은 날짜의 다음 날에 해당하는 날짜도 같은 형식으로 출력합니다.
#
# 단, 윤년은 무시합니다(2월은 항상 28일까지 있다고 가정합니다).

def control_day(num) :
    # 리스트 num을 num2에 복사
    num2 = num[:]
    # 2월인 경우,
    if int(num2[1]) == 2:
        # 날짜가 28일보다 큰 경우
        if int((num2[2])) > 28:
            print("2월은 28일까지만 있습니다.")
        # 날짜가 28일 이하인 경우
        else:
            pass
    # 2월 이외의 월 중 짝수 달의 경우
    elif int(num2[1]) % 2 == 0 :
        # 일자가 31일보다 큰 경우
        if int((num2[2])) > 31 :
            # 출력
            print("짝수 달은 31일까지만 있습니다.")
        # 일자가 31일인 경우
        elif int((num2[2])) == 31 :
            if int((num2[1])) == 12 :
                # 월과 일을 01로 입력
                num2[1] = '1'
                num2[2] = '1'
            else :
                # 월은 1 더하고, 일은 01로 입력
                num2[1] = int((num2[1])) + 1
                num2[2] = '1'
        # if 조건과 elif 조건 이외의 경우
        else :
            pass
    # 2월 이외의 월 중 홀수 달의 경우
    else :
        # 일자가 30일보다 큰 경우
        if int((num2[2])) > 30 :
            # 출력
            print("짝수 달은 30일까지만 있습니다.")
        # 일자가 30일인 경우
        elif int((num2[2])) == 30 :
            # 월은 1 더하고, 일은 1로 입력
            num2[1] = int((num2[1])) + 1
            num2[2] = '1'
        # if 조건과 elif 조건 이외의 경우
        else :
            pass
        pass
    # 반환
    return num2

def print_day(num) :
    # 튜플 리스트 변환
    num = list(num)
    # num을 매개로 받는 control_day 함수 결과를 변수에 입력
    num2 = control_day(num)
    # num 요소만큼 반복
    for i in range(len(num)):
        # 10보다 작을 시
        if int(num2[i]) < 10 :
            # 문자 앞에 0 추가
            num2[i] = '0' + str(num2[i])
        else :
            pass
    else :
        pass

    # num 과 num2 가 동일한 경우
    if num == num2 :
        # 출력
        return print(f"{num2[1]}/{num2[2]}/{num2[0]}")
    # num 과 num2 가 동일하지 않은 경우
    else :
        # 출력
        return (print(f"{num[1]}/{num[2]}/{num[0]}"),
            print(f"{num2[1]}/{num2[2]}/{num2[0]}"))

# 메인 함수 호출
if __name__ == '__main__' :
    # 입력값 변수 정의
    num = input("년을 입력하시오. \n 입력 : "), input("월을 입력하시오. \n 입력 : "), input("일을 입력하시오. \n 입력 : ")
    # 변수에 num 을 매개변수로 받는 print_day 함수 반환값 저장
    print_day(num)