#하노이의 탑 구현하기

def move(no,x,y):
    #원반 no개를 x기둥에서 y기둥으로 옮김
    if no > 1:
        move(no-1, x , 6-x-y)
