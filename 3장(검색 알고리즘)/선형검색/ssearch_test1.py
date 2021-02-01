#seq_search() 함수를 사용하여 실수 검색하기
#내코드
from 선형검색.ssearch_while import seq_search

print("실수를 검색합니다.")
print('주의:"End"를 입력하면 종료합니다.')

array = []
i = 0
while True:
    key = input(f"x[{i}]:")
    if key == "End":
        break
    else:
        key = float(key)
        array.append(key)
ky = float(input("검색할 값을 입력하세요:"))

idx = seq_search(array,ky)
if idx == -1:
    print("해당 값은 없습니다.")
else:
    print(f"검색값은 x[{idx}]에 있습니다.")

"""
#책 코드
from ssearch_while import seq_search

print("실수를 검색합니다.")
print('주의:"End"를 입력하면 종료합니다.')

number = 0
x = []

while True:
    s = input(f"x[{number}]:")
    if s == "End":
        break
    x.append(float(s))
    number += 1

key = float(input("검색할 값을 입력하세요:"))

idx = seq_search(x,key)
if idx == -1:
    print("해당 값은 없습니다.")
else:
    print(f"검색값은 x[{idx}]에 있습니다.")
"""