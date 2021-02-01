import copy
def seq_search(seq,key):
    #seq를 복사
    a = copy.deepcopy(seq) #보초 key를 추가
    a.append(key)
    #보초를 추가한 a라는 새로운 배열 생성
    i = 0
    while True:
        if a[i] == key:
            break #찾고자 하는 값 찾으면
        i += 1
    if i == len(seq):
        return -1
    else:
        return i
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