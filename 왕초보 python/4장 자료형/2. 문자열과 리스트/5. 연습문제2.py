# 다음과 같은 사람들이 있습니다.
#
# 뉴진스를 좋아하는 사람: 철수, 영희, 민수, 지현, 서연
# 아이브를 좋아하는 사람: 영희, 민수, 지수, 서연, 하나
# 에스파를 좋아하는 사람: 철수, 지현, 지수, 서연, 나영
# 이 중에서 뉴진스와 아이브를 모두 좋아하지만 에스파는 좋아하지 않는 사람은 누구일까요?

# 리스트 정의
fans_newjeans = ['철수', '영희', '민수', '지현', '서연']
fans_ive = ['영희', '민수', '지수', '서연', '하나']
fans_espa = ['철수', '지현', '지수', '서연', '나영']

# 출력
print("뉴진스와 아이브를 모두 좋아하지만 에스파는 좋아하지 않는 사람은?")

# 리스트 초기화
fans_newive = []

# 반복문 활용
for i in fans_newjeans :
    if (i in fans_ive) and (i not in fans_espa) :
        print(i)
    else :
        pass
else :
    pass

# in, append, join 활용
for i in fans_newjeans :
    if (i in fans_ive) and (i not in fans_espa):
         fans_newive.append(i)
    else :
        pass
else :
    pass

# join 활용
result = ", ".join(fans_newive)
# 출력
print(result)

