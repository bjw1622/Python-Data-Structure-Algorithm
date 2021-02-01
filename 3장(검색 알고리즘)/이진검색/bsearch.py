def bin_search(array,key):
    #인덱스 번호 나타내기
    first = 0
    last = len(array) - 1

    while True:
        mid = first + last // 2
        if array[mid] == key:
            return mid

        elif array[mid] > key:
            last = array[mid] - 1

        elif array[mid] > key:
            first = array[mid] + 1

        else:
            return -1

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요:'))
    print("배열 데이터를 입력하세요.")
    array = []
    for i in range(num):
        value = int(input(f"x[{i}]:"))
        array.append(value)
    array.sort()

    key = int(input("검색할 값을 입력하세요:"))

    result = bin_search(array,key)

    if result == -1:
        print("검색값을 갖는 원소가 존재하지 않습니다,")
    else:
        print(f"검색값은 x[{result}]에 있습니다.")