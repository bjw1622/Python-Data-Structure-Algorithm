"""
#순차검색,선형검색
def find(array,key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    else:
        return -1

number = int(input("입력하고싶은 갯수를 입력하시오:"))
array = []

for i in range(number):
    value = int(input(f"x[{i}]"))
    array.append(value)

key = int(input("찾고자하는 값을 입력하시오:"))
result = find(array,key)

if array[result] == key:
    print(f"{key}값은 x[{result}]에 존재합니다.")
else:
    print("찾고자하는 값은 존재하지 않습니다.")
"""

def find(array,key):
    #array는 list key는 찾고자 하는 값
    for i in range(len(array)):
        if array[i] == key:
            return i
    #for문을 다 돌고나서 없으면 -1을 반환
    else:
        return -1
    #찾고자 하는 값의 인덱스를 반환

number = int(input("배열의 길이를 입력하시오.:"))
array = []

for i in range(number):
    value = int(input(f"x[{i}]:"))
    array.append(value)

key = int(input("찾고자하는 값을 입력하시오.:"))
result = find(array,key)

if array[result] == key:
    print(f"{key}값은  x[{result}]에 존재합니다.")
else:
    print("찾고자하는 값은 존재하지 않습니다.")