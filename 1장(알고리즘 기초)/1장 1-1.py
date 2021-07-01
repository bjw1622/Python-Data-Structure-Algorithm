print("세 정수의 최댓값을 구합니다.")

a = int(input("정수 a의 값을 입력하세요:"))
b = int(input("정수 b의 값을 입력하세요:"))
c = int(input("정수 c의 값을 입력하세요:"))

max_data = max(a,b,c)

print(f"최댓값은 {max_data}입니다.")

"""
책 예제
max = a
if b > max:
    max = b
if c > max:
    max = c
    
순서대로 처리되는 구조를 순차구조.

조건식으로 평가한 결과에 따라 프로그램의 실행 흐름이 변경되는건 선택 구조

"""