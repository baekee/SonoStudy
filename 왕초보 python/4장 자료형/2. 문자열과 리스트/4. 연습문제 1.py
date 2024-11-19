# 성적표 만들기
# chulsu, yonghee, yong, minsu 학생의 국, 영, 수 성적을 넣어 student 리스트에 넣은 뒤,
# 총점 및 평균이 나오도록 출력해보기.

# 국영수 성적을 원소로 하는 리스트를 학생 이름 변수에 정의
chulsu = [90, 85, 70]
younghee = [88, 79, 92]
yong = [100, 100, 100]
minsu = [90, 60, 70]

# 학생 이름 리스트를 students 변수에 정의
students = [chulsu, younghee, yong, minsu]
names = ['chulsu', 'younghee', 'yong', 'minsu']
i = 0

# 학생 성적 출력
for scores in students :
    print(scores)

for scores in students :

    # 총점 구하기
    total = 0
    for s in scores:
        total = total + s

    # 평균점수 구하기
    average = round(total / 3, 2)

    print(f"{names[i]} 학생의 국영수 성적은 {scores}이고, 총점은 {total}점이고, 평균점수는 {average}점입니다.")

    i += 1