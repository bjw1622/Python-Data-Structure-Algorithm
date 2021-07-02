import random
from max import max_of

print("난수의 최댓값을 구합니다.")
number = int(input("난수의 개수를 입력하세요:"))
minimize = int(input("난수의 최솟값을 입력하세요:"))
maxmize = int(input("난수의 최댓값을 입력하세요:"))

data = []
for i in range(number):
    data.append(random.randint(minimize,maxmize))

print(data)
print(f"이 가운데 최댓값은 {max_of(data)}입니다.")
