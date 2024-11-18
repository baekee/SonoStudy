from traceback import print_tb
from xmlrpc.client import boolean

for x in range(5) :
    print(x)
else :
    print("모든 원소 출력 완료")

# if문의 else 에서 break 로 인해 종료되므로, for 문의 else 실행 X
for x in range(5) :
    if x % 3 :
        print(x)
    else :
        print("중도 완료 처리")
        break
else :
    print("모든 원소 출력 완료")


coutdown = 5
while coutdown > 0 :
    print(coutdown)
    coutdown -= 1
    if input() == '중단' :
        break
else :
    print("발사!")