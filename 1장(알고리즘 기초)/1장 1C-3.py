print("2자리 양수를 입력하세요.")

while(True):
    number = int(input("값을 입력하세요:"))
    if (number >=10 and number <100):
        break
print(f"입력받은 양수는 {number}입니다.")