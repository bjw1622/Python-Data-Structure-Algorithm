def recur(n):
    if n > 0:
        recur(n-1)
        print(n)
        recur(n-2)

x = int(input('정수값을 입력하세요:.'))

recur(x)

#재귀 분석 방법에는 2가지 상향식 , 하향식
#상향식은 밑에서부터 위로
#하향식은 가장 위쪽에 있는거부터 계단식으로 처리