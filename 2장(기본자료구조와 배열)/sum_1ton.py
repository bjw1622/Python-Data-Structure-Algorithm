def sum_1ton(n):
    result = 0
    i = 1
    while i < n+1:
        result += i
        i += 1
    return result
x = int(input("x의 값을 입력하세요.:"))
print(f"1부터 {x}까지 정수의 합은 {sum_1ton(x)}입니다.")