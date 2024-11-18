# 태어난 해를 네 자리 숫자로 입력하면 한국 나이를 반환하는 1. 함수 korean_age()를 작성하세요.

def korean_age(x) :
    from datetime import datetime
    today = datetime.today().year
    age = today - x + 1
    return age

print(korean_age(int(input("태어난 해를 네자리 숫자로 입력해주세요. \n" + "입력 : "))))
