# 튜플

# 값 전환
a = 10
b = 20
temp = a               # a 값을 temp에 저장   (temp = 10)
a = b                  # b 값을 a에 저장      (a = 20)
b = temp               # temp 값을 b에 저장   (b = 10)
print(a, b)

c = 10
d = 20
c, d = d, c
print(c, d)

# 매개변수 x,y를 받는 magu_print 함수 정의
# 인자 2개 이후의 수들은 튜플에 삽입됨
# * 인자는 이후에 들어오는 인자들이 모두 튜플에 삽입된다는 것임
def magu_print(x, y, *rest):
     print(x, y, rest)

magu_print(1, 2, 3, 5, 6, 7, 9, 10)

# 문법
# 괄호가 있어도 되고 없어도 됨
t = ('a', 'b', 'c')

# 원소가 없을 경우, 반드시 괄호를 써 주어야 함
empty = ()

# 원소를 하나만 가진 튜플의 경우 반드시 콤마(,) 를 찍어주어야 함
one = 5,
print(one)

# 원소값 변경이 불가하므로, 오려붙이는 방식으로 수정함
p = (1,2,3)
q = p[:1] + (5,) + p[2:]
print(q)

r = p[:1], 5, p[2:]
print(r)

# 리스트와 튜플 전환
p = (1, 2, 3)
q = list(p)                  # 튜플 p로 리스트 q를 만듦
print(q)

r = tuple(q)                 # 리스트 q로 튜플 r을 만듦
print(r)
