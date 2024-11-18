# 리스트

prime = [3, 7, 11]
# 리스트에 원소 추가 .append(원소)
prime.append(5)
print(prime)

# 리스트 정렬 .sort()
prime.sort()
print(prime)

# 원소 삽입 .insert(인덱스 값, 원소 값)
prime.insert(0, 2)
print(prime)

# 원소 삭제
del prime[4]
print(prime)

a = prime.pop()
print(prime)
print(a)

# 원소에 새로운 값 지정
prime[0] = 1
print(prime)

# 리스트에 리스트 넣기
orders = ['potato', ['pizza', 'Coke', 'salad'], 'hamburger']
print(orders[1])
print(orders[1][2])

# 리스트로 행렬표현하기
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)