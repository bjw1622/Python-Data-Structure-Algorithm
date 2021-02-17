def factorial(value):
    if value == 0:
        return 1
    else:
        return value * factorial(value-1)

if __name__ == '__main__':
    n = int(input('출력할 팩토리얼값을 입력하세요.:'))
    print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')``````````````````````````````````````````````````````````````