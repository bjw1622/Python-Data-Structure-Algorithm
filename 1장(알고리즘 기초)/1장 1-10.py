print("a부터 b까지 정수의 합을 구합니다.")
a = int(input("정수 a를 입력하세요:"))
b = int(input("정수 b를 입력하세요:"))

sum = 0
if a > b:
    a , b = b, a
if (a == b):
    print(f"{a} = {b}")
elif (a != b):
    sum = a + b
    print(f"{a} + {b} = {sum}")