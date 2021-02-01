print("+와 -를 번갈아 출력합니다.")

number = int(input("몇 개를 출력할까요?:"))

for i in range(1,number+1):
    if(i % 2 != 0):
        print("+",end="")
    else:
        print("-",end="")