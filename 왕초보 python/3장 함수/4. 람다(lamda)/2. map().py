# 리스트 재정의 1. 함수
print(list(map(lambda x : x ** 2, range(5))))    # 파이썬 2 및 파이썬 3

# 일반 함수로 map 함수 형식 구현해보기
def like_map() :
    l = []
    for i in range(5) :
        l.append(i ** 2)
    else :
        pass

    return l

if __name__ == '__main__':
    print(like_map())
