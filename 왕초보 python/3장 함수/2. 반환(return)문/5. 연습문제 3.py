# 원금(p), 단리 이율(r), 기간(t)이 주어졌을 때 원리금을 계산하는 1. 함수 simple_interest_amount()를 작성하세요.

def simple_interest(p, r, t) :
    return p * r * t

def simple_interest_amount(p, r, t) :
    return p * (1 + r * t)

def main() :
    print("만기 시 받을 수 있는 이자 : ")
    print(simple_interest(10000000, 0.03875, 5))
    print(simple_interest(1100000, 0.05, 5/12))

    print("\n")

    print("원금과 이자를 합한 총액인 원리금 : ")
    print(simple_interest_amount(10000000, 0.03875, 5))
    print(simple_interest_amount(1100000, 0.05, 5 / 12))

if  __name__ == '__main__' :
    main()