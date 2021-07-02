from typing import Any, Sequence

def maximun(data):
    return max(data)

print("배열의 최댓값을 구합니다.")
number = int(input("원소 수를 입력하세요:"))
data = [None] * number
for i in range(number):
    num = int(input(f"x[{i}]값을 입력하세요.:"))
    data[i] = num

print(f"최댓값은 {maximun(data)}입니다.")