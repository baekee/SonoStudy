# 1,000 단위는 k , 1,000,000 단위는 M, 1,000,000,000 단위는 G 단위로 표현하시오.

num = int(input())
result = str(num)

if num >= 1000000000 :
    result = str(num // 1000000000) + 'G'
elif num >= 1000000 :
    result = str(num // 1000000) + 'M'
elif num >= 1000 :
    result = str(num // 1000) + 'k'
elif num >= 0 :
    pass

print(result)