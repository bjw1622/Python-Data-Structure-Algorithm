def mid(a,b,c):
    if (a > b and a < c):
        return a
    elif (a > c and a < b):
        return a

    elif (b > a and b < c):
        return b
    elif (b > c and b < a):
        return b

    elif(c > a and c < b):
        return c
    elif(c > b and c < a):
        return c

print("세 정수의 중앙값을 구합니다.")
a = int(input("정수 a의 값을 입력하세요:"))
b = int(input("정수 b의 값을 입력하세요:"))
c = int(input("정수 c의 값을 입력하세요:"))
print(f"중앙값은 {mid(a,b,c)}입니다.")