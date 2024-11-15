# input()으로 사용자의 나이를 입력받은 후, 다음 표의 어느 세대에 속하는지 출력하세요. 입출력 문구는 자유롭게 지으면 됩니다.

print('출생년도 4자리를 입력해주세요 \n' + '입력 : ')

age = int(input())
# generation = ''
generation = None

if age > 1997 :
    generation = 'Z'
# elif 1981 <= age < 1997 :
elif 1981 <= age :
    generation = '밀레니얼'
# elif 1965 <= age < 1981 :
elif 1965 <= age :
    generation = 'X'
# elif 1946 <= age < 1965 :
elif 1946 <= age :
    generation = '베이비붐'
# elif 1925 <= age < 1946 :
elif 1925 <= age :
    generation = '침묵'
else :
    generation = '가장 위대한'

# print('당신은 ' + generation  + ' 세대입니다.')
print(f'당신은 {generation} 세대 입니다.')