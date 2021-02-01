"""
내코드
print("배열의 최댓값을 구합니다.")
number = int(input("원소 수를 입력하세요:"))
array = []
for i in range(0,number):
    num = int(input(f"x[{i}]값을 입력하세요:"))
    array.append(num)
print(f"최댓값은 {max(array)}입니다.")
"""
#책 예제
from typing import Any, Sequence
#Any는 제약이 없는 임의의 자료형을 말하고 , 시퀀스형은 리스트 바이트 문자열 튜플 바이트열 등을 말한다.
def max_of(a:Sequence): #건네받는 매개변수 a의 자료형은 시퀀스 , 반환하는것은 임의의 자료형인 Any이다.
    maximum = a[0]
    for i in range(1,len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    print("배열의 최댓값을 구합니다.")
    num = int(input("원소 수를 입력하세요.:"))
    x = [None] * num #원소 수가  num인 리스트 생성

    for i in range(num):
        x[i] = int(input(f"x[{i}값을 입력하세요.:"))

    print(f"최댓값은 {max_of(x)}입니다.")