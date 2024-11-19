# 주사위 두 개가 있습니다.
# 한 개는 평범한 주사위인데, 다른 한 개의 각 면에는 2에서 13까지의 소수가 적혀 있습니다.
# 아래 코드는 두 주사위의 눈을 튜플 dice1과 dice2로 나타냅니다.
# 두 주사위를 던졌을 때 눈의 합으로 나올 수 있는 숫자를 모두 출력하세요.
# 단, 같은 숫자는 한 번만 출력합니다.

# itertools 함수 import
import itertools

# 튜플 정의
dice1 = (1, 2, 3, 4, 5, 6)
dice2 = (2, 3, 5, 7, 11, 13)

# 각 튜플 인자 합한 수 result 변수에 저장 및 중복 값 set()로 제거
result = set(map(lambda x: x[0] + x[1], set(itertools.product(dice1, dice2))))

if __name__ == '__main__' :
    # 출력
    print(result)