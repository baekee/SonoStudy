# 문자열

# 슬라이싱
x = 'banana'

print(x[0])
print(x[2:4])
print(x[:3])
print(x[3:])
print(x[::-1])

# 문자열 글자를 인덱스를 활용하여 바꿀 수 있는가
# TypeError: 'str' object does not support item assignment 에러 발생
# ☞ 안됨
# x[0] = 'n'
# print(x)

x = 'n' + x[1:]
print(x)

# 문자열 일부 복사
p = 'Python'
print(p[0:2])
print(p[:2])

# 다른 문자열과 합치기
w = 'Hello world!'
print(w[:6] + p + '!')

# 음수 인덱스 사용
print(w[-1:])
print(w[:6] + p + w[-1:])

# replace() 메서드 사용
print(w.replace('world', 'Python'))

# 문자열 전부 복사
print(p[:])

# 역순으로 복사
print(p[::-1])

# 리스트 슬라이싱

N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(N[0])  # 0번(첫 번째) 원소
print(N[0:5]) # 0번부터 5번 앞(4번)까지
print(N[:5]) # 처음부터 5번 앞까지
print(N[5:]) # 5번부터 끝까지
print(N[-3:]) # 뒤에서 3번째부터 끝까지
print(N[::-1]) # 역순으로

fruit = ['apple', 'banana', 'cherry', 'mango', 'orange']
print(fruit[0:2])
print(fruit[2])
print(fruit[2:])

# find()
# 문자열에 어떤 글자가 몇 번째 자리(인덱스 값)에 있는지 확인
s = "hello Python!"
print(s.find('P'))
print(s[0:6])

h = s[0:6]
print(h)

print(h[0:5])

# 공백 제거
print(h.rstrip())

