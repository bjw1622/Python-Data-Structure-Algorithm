from typing import Any, MutableSequence

def reverse_array(a:MutableSequence) -> None:
    n = len(a)
    for i in range(n//2):
        a[i] , a[n-i-1] = a[n-i-1] , a[i]


if __name__ == '__main__':
    print("배열 원소를 역순으로 정렬합니다.")
    number = int(input("원소 수를 입력하세요.:"))
    arr = []
    for i in range(number):
        num = int(input(f"x[{i}]값을 입력하세요.:"))
        arr.append(num)
    print("배열 원소를 역순으로 정렬했습니다.")
    reverse_array(arr)
    for i in range(len(arr)):
        print(f"x[{i}] = {arr[i]}")