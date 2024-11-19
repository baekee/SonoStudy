# 소수(素數, prime number)는 1 과 그 자체만을 인수(factor)로 갖는 수입니다.
# 또는 “1보다 큰 자연수 중 1과 자기 자신만을 약수로 가지는 수”라고 설명하기도 합니다.
#
# 다음은 소수입니다.
#
# ```
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...
#
# ```
# 소수를 구하는 방법은 다음과 같습니다.
#
# > 찾고자 하는 범위의 자연수를 나열한다.2부터 시작하여, 2의 배수를 지워나간다.다음 소수의 배수를 모두 지운다.
# >
#
# 다음은 파이썬 셸에서 수작업으로 10 이하의 소수를 구하는 예입니다.
#
# ```python
# >>> L = list(range(2, 11))             # 찾고자 하는 범위의 자연수를 나열
# >>> L
# [2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> L.remove(4); L.remove(6); L.remove(8); L.remove(10) # 2의 배수를 지움
# >>> L.remove(9)                                         # 3의 배수를 지움
# >>> L                                                   # 결과
# [2, 3, 5, 7]
#
# ```
#
# 이와 같은 방식으로 찾고자 하는 범위(예: 30 이하)의 소수를 구하는 것이 문제입니다. 수작업으로 하지 말고 반복문을 사용하세요.

def is_prime(n) :
    # 1 이하의 숫자는 소수가 아님
    if n <= 1 :
        return False
    # 소수 판별을 위한 계산 최적화
    for i in range(2, int(n ** 0.5) + 1) :
        # n이 i로 나누어떨어지면 소수가 아님
        if n % i == 0 :
            return False
    # 나누어떨어지는 수가 없으면 소수임
    return True

def find_prime_number(limit) :
    primes = []
    for num in range(2, limit + 1) :
        if is_prime(num):
            primes.append(num)
    return primes


def sieve_of_eratosthenes(limit):
    # True로 초기화된 리스트 생성 (2부터 limit까지 모든 수가 소수라고 가정)
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False  # 0과 1은 소수가 아님

    for start in range(2, int(limit ** 0.5) + 1):
        if is_prime[start]:  # start가 소수일 경우
            # start의 배수들은 소수가 아님
            for multiple in range(start * start, limit + 1, start):
                is_prime[multiple] = False

    # 소수 리스트 반환
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

if __name__ == '__main__' :
    from time import process_time
    num = int(input('Enter a number: '))
    start = process_time()
    # print(find_prime_number(num))
    find_prime_number(num)
    end = process_time()
    print(f'기존 함수 처리 시간 : {end - start}')
    start = process_time()
    sieve_of_eratosthenes(num)
    # print(sieve_of_eratosthenes(num))
    end = process_time()
    print(f'에라토스테네스이 체 알고리즘 처리 시간 : {end - start}')