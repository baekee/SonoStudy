# stem_leaf에 데이터를 채우는 프로그램을 작성하세요. 데이터가 채워진 결과는 다음과 같습니다.

# >>> stem_leaf
# [[0, 0, 2, 4, 7, 7, 9], [1, 1, 3, 8], [0]]
# >>> stem_leaf[0]
# [0, 0, 2, 4, 7, 7, 9]
# >>> stem_leaf[1]
# [1, 1, 3, 8]
# >>> stem_leaf[2]
# [0]
score = [0, 0, 2, 4, 7, 7, 9]
score += [11, 11, 13, 18]
score += [20]

def method_stem_leaf() :
    stem_leaf = [[], [], []]
    for i in score :
        # if i < 10 :
        #     stem_leaf[0].append(i)
        # elif i < 20 :
        #     stem_leaf[1].append(i)
        # else :
        #     stem_leaf[2].append(i)
        d, m = divmod(i, 10)
        stem_leaf[d].append(m)
    else :
        pass

    return stem_leaf

# stem_leaf를 다음과 같은 형태로 프린트하는 프로그램을 작성하세요.

# 0: [0, 0, 2, 4, 7, 7, 9]
# 1: [1, 1, 3, 8]
# 2: [0]

def method_stem_leaf_print(stem_leaf) :
    # j = 0
    # for i in stem_leaf :
    #     print(f"{j}: {stem_leaf[j]}")
    #     j += 1
    for i in range(len(stem_leaf)):
        print(f'{i}: {stem_leaf[i]}')
    else :
        pass

if __name__ == '__main__' :
    print(method_stem_leaf())
    method_stem_leaf_print(method_stem_leaf())