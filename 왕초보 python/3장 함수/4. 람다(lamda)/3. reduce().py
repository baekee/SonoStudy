from functools import reduce
print(reduce(lambda x, y: x + y, [0, 1, 2, 3, 4]))

# 문자열 역순 반환 1. 함수
print(reduce(lambda x, y: y + x, 'abcde'))