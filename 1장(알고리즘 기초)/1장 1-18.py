import random
n = int(input("난수의 개수를 입력하세요:"))

for i in range(n):
    r = random.randint(10,99)
    print(r,end=" ")
    if r == 13:
        print("프로그램을 중단합니다")
        break
print("\n난수의 생성을 종료합니다.")