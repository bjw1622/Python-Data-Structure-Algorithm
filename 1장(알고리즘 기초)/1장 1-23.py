print("오른쪽 아래가 직각인 이등변 삼각형을 출력합니다.")
number = int(input("짧은 변의 길이를 입력하세요:"))
for i in range(1,number+1):
    print(" "*(number-i) + "*"*i)
