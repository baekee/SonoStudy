# 딕셔너리 자료형 형식으로 선언
smalldic = {'dictionary': 'reference', 'python': 'snake'}
print(smalldic['python'])
print(smalldic)

# 원소 삭제
del smalldic['dictionary']
print(smalldic)

family = {'mom': 'Kim', 'dad': 'Choi', 'baby': 'Choi'}
# 키을 얻는 함수 .keys()
print(family.keys())
# 값을 얻는 함수 .values()
print(family.values())
# 원소(키/값)들을 얻는 함수 .items()
print(family.items())

# 키 포함 여부 확인
print('dad' in family)
print('sister' in family)