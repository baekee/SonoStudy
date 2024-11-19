# 세트 정의
fruits = {'apple', 'banana', 'orange'}
# 출력
print(fruits)
# 인자 추가
fruits.add('mango')
# 출력
print(fruits)

# 세트 초기화
companies = set()
# 인자 추가
companies = {'apple', 'microsoft', 'google'}
# 출력
print(companies)

# 타입 반환
print(type(fruits), type(companies))

# 교집합
print(fruits & companies)

# 합집합
print(fruits | companies)

list_of_sets = [fruits, companies]
# 교집합
print(set.intersection(*list_of_sets))
# 합집합
print(set.union(*list_of_sets))

# 중복 원소 제거에 set() 활용
alphabet = list('google')
print(alphabet)
print(set(alphabet))

# 차집합
S1 = {1, 2, 3, 4, 5, 6, 7}
S2 = {3, 6, 9}
print(S1 - S2)