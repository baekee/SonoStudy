# 놀이 기구의 이름과 키 제한을 나타낸 문자열을 입력받아서,
# 놀이 기구의 이름, 탑승 가능한 키의 하한(下限)과 상한(上限)을 각 행에 출력합니다.

def read(text):
    text = text.split(':')
    ridename = text[0].strip()

    if "~" in text[1] :
        cmmin = int((text[1].split('~')[0].replace('cm', '')).strip())
        cmmax = int((text[1].split('~')[1].replace('cm', '')))
    else :
        if "이상" in text[1] :
            cmmin = int((text[1].split('cm')[0]).strip())
            cmmax = None
        elif "이하" in text[1] :
            cmmin = None
            cmmax = int((text[1].split('cm')[0]).strip())
        elif "-" in text[1] :
            cmmin = None
            cmmax = None
        else :
            print("입력값을 이상, 이하 혹은 -로 표현해주십니오.")
            pass

    return ridename, cmmin, cmmax


if __name__ == "__main__":
    ridename, cmmin, cmmax = read(input())
    print("이름:", ridename)
    print("하한:", cmmin)
    print("상한:", cmmax)