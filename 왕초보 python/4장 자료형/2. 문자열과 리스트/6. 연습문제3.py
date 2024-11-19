# 회문 판별 함수 만들기
# 회문이란?
# 거꾸로 배열해도 같은 단어 혹은 문장이 되는 것
# ex) Anna, Civic, Kayak, Level

# 주어진 단어가 회문인지 판별하는 함수 palindrome()을 작성하세요.
# 단, 문자열 입력은 모두 소문자로 이뤄지며 공백을 포함하지 않는다고 가정합니다.

def palindrome(x) :

    if x == x[::-1] :
        return True
    else :
        return False


# 대문자와 소문자가 섞여 있더라도 회문으로 판정하도록 함수를 개선하세요.

def palindrome(x) :

    x = x.lower()

    if x == x[::-1] :
        return True
    else:
        return False

# 공백이 섞여 있더라도 회문으로 판정하도록 함수를 개선하세요.
def palindrome(x) :

    x = x.lower().replace(' ', '')

    if x == x[::-1]:
        return True
    else:
        return False

if __name__ == '__main__' :
    print(palindrome('anna'))
    print(palindrome('banana'))
    print(palindrome('Anna'))
    print(palindrome('My gym'))