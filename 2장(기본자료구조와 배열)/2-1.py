print("학생 그룹 점수의 합계와 평균을 구합니다.")
total = []
result = 0
for i in range(1,6):
    score = int(input(f"{i}번 학생의 점수를 입력하세요:"))
    total.append(score)
    result += score

print(f"합계는 {result}점입니다.")
print(f"평균은 {result/5}점입니다.")
