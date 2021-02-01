print("1부터 n까지 정수의 합을 구합니다.")
while(True):
    number = int(input("n값을 입력하세요:"))
    if number > 0:
        sum = 0
        for i in range(1,number+1):
            sum += i
        break;

    else:
        continue

print(f"1부터 10까지 정수의 합은 {sum}입니다.")