# input()으로 사용자로부터 입력받은 정수를 계속 더해나가다가, 음수가 입력되면 중단하고 그 전까지 계산한 값을
# 출력하는 파이썬 스크립트를 작성하세요.

# numlist = list()
# i = 0
sum = 0

while True :
    num = int(input('숫자를 입력해주세요 \n' + '입력 : '))

    # 값이 양수인 경우
    if num >= 0 :
        # numlist.append(num)
        # sum = sum + int(numlist[i])
        # i += 1
        sum += num

    # 값이 음수인 경우
    else :
        # numlist.append(num)
        # sum = sum + int(numlist[i])
        # i += 1
        sum += num
        print(sum)
        break



