#while문을 for문으로 변환

def seq_search(a,key):
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

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