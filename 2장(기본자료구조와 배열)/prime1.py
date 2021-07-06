# 1000 이하의 소수를 나열하기

for i in range(2,1001):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)
