counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1
# 4이상의 짝수는 2로 다 나누어지기 때문에 소수가 아니다.

for n in range(3,1001,2):
    #홀수들은 2로 나누어 떨어지지 않기 때문에!
    for i in range(1,ptr):
        counter += 1
        if n % prime[i] == 0:
            break
    else:
        prime[ptr] = n
        ptr += 1

for i in range(ptr):
    print(prime[i])
print(f"나눗셈을 실행한 횟수:{counter}")