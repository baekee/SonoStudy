# 문자열을 리스트로 변환

# 리스트 변수 정의
characters = []
# 문자열 변수 정의
sentence = 'Be happy!'

# 문자열 sentence 의 항목 char 에 대하여 반복
for char in sentence:
    # 리스트 characters 에 각 항목 char 추가
    characters.append(char)

# 출력
print(characters)


# 문자열을 리스트로 변환
print(list('Be happy!'))


# 숫자열을 문자열로 바꾸기
my_int = 123
print(type(my_int))

str(my_int)
print(type(str(my_int)))

my_str = str(my_int)
print(my_str)

# 문자열을 숫자로 바꾸기
print(int('123'))
print(float('123'))


# 리스트 원소들의 합 구하기
one_to_ten = list(range(1, 11))
print(one_to_ten)

# 원소들의 합 구하기
print(sum(one_to_ten))

# 1부터 10까지 더한 값 구하기
# 매개변수가 없는 함수 plus_one_ten 정의
def plus_one_ten() :
    # 누적함수 reduce import
    from functools import reduce
    # 리스트 초기화
    one_to_ten = []
    # 변수 정의
    i = 0
    # 1이상 10미만 범위 안의 항목 i 에 대하여 반복
    for i in range(i + 1, i + 11) :
        # one_to_ten 리스트에 항목 추가
        one_to_ten.append(i)
    # for 반복문 완료 시
    else :
        # 아무 동작도 하지 않고 넘김
        pass

    # plus_one_ten 변수에 람다 표현식을 이용한 reduce 함수로 one_to_ten 리스트에 있는 원소 값 더하기
    plus_one_ten = reduce(lambda x, y: x + y, one_to_ten)
    # plus_one_ten 변수 반환
    return plus_one_ten

# 메인 함수 호출
if '__main__' == __name__ :
    # 출력
    print(plus_one_ten())
