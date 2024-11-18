# 매개변수로 받은 정수를 한국어로 표기한 문자열을 반환하는 1. 함수 korean_number()를 정의하세요.
# 단, 매개변수는 1 이상 10 이하의 정수라고 가정합니다.

def korean_number(x) :

    if x == 1 :
        x = '일'
        return x
    elif x == 2 :
        x = '이'
        return x
    elif x == 3 :
        x = '삼'
        return x
    elif x == 4 :
        x = '사'
        return x
    elif x == 5 :
        x = '오'
        return x
    elif x == 6 :
        x = '육'
        return x
    elif x == 7 :
        x = '칠'
        return x
    elif x == 8 :
        x = '팔'
        return x
    elif x == 9 :
        x = '구'
        return x
    elif x == 10 :
        x = '십'
        return x
    else :
        pass

print(korean_number(int(input())))