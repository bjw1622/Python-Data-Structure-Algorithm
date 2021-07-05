from max import max_of

print("배열의 최댓값을 구합니다.")
print('주의: "End"를 입력하면 종료합니다.')
x = 0
data = []
while True:
    number = input(f"x[{x}]값을 입력하세요:")
    if number == "End":
        break
    x += 1
    data.append(int(number))

print(f"{x}개를 입력했습니다.")
print(f"최댓값은 {max_of(data)}입니다.")