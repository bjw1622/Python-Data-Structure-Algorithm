# index 함수로 검색하기.
# array = [2,3,4,8,9,1,2,7,8,3,2,8,2]
# array.sort()
# print(array.index(1))

def bin_search(a,key):
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc +1

        else:
            pr = pc - 1

        if pl > pr:
            break
            return -1

if __name__ == "__main__":
    num = int(input("원소 수를 입력하세요.:"))
    x = [None] * num
    print("배열 데이터를 오름차순으로 입력하세요.")
    x[0] = int(input('x[0]:'))
    for i in range(1,num):
        while True:
            x[i] = int(input(f"x[{i}]:"))
            if x[i] >= x[i-1]:
                break
    ky = int(input('검색할 값을 입력하세요:'))
    idx = bin_search(x,ky)

    if idx == -1:
        print(f"검색값을 갖는 원소가 존자하지 않습니다.")

    else:
        print(f"검색값은 x[{idx}]에 있습니다.")


# number = int(input("원소 수를 입력하세요:"))
# print("배열 데이터를 오름차순으로 입력하세요.")
# array = [None] * number
# for i in range(number):
#     data = int(input(f"x[{i}]:"))
#     array[i] = data
# find = int(input("검색할 값을 입력하세요.:"))
#
# pl = array[len(array)-1]
# pr = 0
# pc = len(array) // 2
# while True:
#     if find == array[pc]:
#         break
#     elif array[pc] > find:
#         pl = pc - 1
#         pc = (pl-pr) // 2
#     elif find > array[pc]:
#         pr = pc + 1
#         pc = (pl - pr) // 2
#
# print(f"검색값은 x[{pc}]에 있습니다.")