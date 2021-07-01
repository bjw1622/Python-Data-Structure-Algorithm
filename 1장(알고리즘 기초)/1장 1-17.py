area = int(input("직사각형의 넓이를 입력하세요:"))

for i in range(1,(area//2)+1):
    #반복 막는 조건문
    if i * i >area :
        break
    elif i * (area // i) == area:
        print(f"{i} x {area//i}")
