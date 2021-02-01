count = 0
for i in range(2,1001):
    for j in range(2,i):
        count += 1
        if i % j == 0:
            break
    else:
        print(i)
print(f"나눗셈을 실행한 횟수:{count}")
