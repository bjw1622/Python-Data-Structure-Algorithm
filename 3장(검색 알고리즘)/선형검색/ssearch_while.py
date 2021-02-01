"""
내가 만든 코드(이진 탐색)
number = int(input("원소 수를 입력하세요:"))
array = [None] * number #입력한 원소 수 만큼 생성
for i in range(number):
    array[i] = int(input(f"x[{i}]:"))
find = int(input("검색할 값을 입력하세요.:"))
for i in range(number):
    if array[i] == find:
        print(f"검색값은 x[{i}]에 있습니다.")
        break
"""
#책 예제 코드

def seq_search(a,key):
    i = 0

    while True:
        if i == len(a): #원하는 값이 없을때 -1을 반환
            return -1
        if a[i] == key:
            return i
        i += 1

if __name__ == '__main__':
    num = int(input("원소 수를 입력하세요"))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input("검색할 값을 입력하세요.:"))

    idx = seq_search(x,ky) #x리스트에서 ky값 찾기

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')