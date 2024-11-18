# 문자열

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

