import random
from max import max_of

print('난수의 최댓값을 구합니다.')
num = int(input("난수의 개수를 입력하세요.:"))
lo = int(input("난수의 최솟값을 입력하세요.:"))
hi = int(input("난수의 최댓값을 입력하세요.:"))
x = []  #원소 수가 num인 리스트를 생성

for i in range(num):
    x.append(random.randint(lo,hi))

print(f"{x}")
print(f"이 가운데 최댓값은 {max_of(x)}입니다.")