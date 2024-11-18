# 양(陽)의 정수를 입력받아, 그 수가 몇 자리 숫자인지 출력하는 1. 함수 numOfDigits()를 만들어 보세요.

def numOfDigits(num) :
    print("입력하신 숫자의 자리수는", len(num), "입니다.")

num = input("양의 정수를 입력해주세요. \n" + "입력 : ")
numOfDigits(num)