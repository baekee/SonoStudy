# 정수 num을 매개변수로 받아 각 자리 숫자(digit)의 합을 계산하는 sumOfDigits() 함수를 작성하세요.
# 단, 나눗셈을 이용하지 말고 리스트를 사용해서 풀어보세요.

def sumOfDigits(num) :
    L = []
    for i in num :
        L.append(int(i))
    else :
        pass

    return sum(L)


if __name__ == '__main__' :
    num = input('Enter a number: ')
    print(sumOfDigits(num))