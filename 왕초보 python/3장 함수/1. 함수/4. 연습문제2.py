# 2단부터 9단까지 출력하기

def multi(m):
    print(f'[{m} 단]')
    for n in range(1, 10):
        print(f'{m} * {n} = {m * n:2d}')

for x in range(2, 10) :
    multi(x)