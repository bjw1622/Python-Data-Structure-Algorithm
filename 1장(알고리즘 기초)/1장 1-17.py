area = int(input("직사각형의 넓이를 입력하세요:"))

for i in range(1,area+1):
    for j in range(1,area+1):
        if i > j:
            continue
        else:
            if i * j == area:
                print(f"{i}x{j}")
