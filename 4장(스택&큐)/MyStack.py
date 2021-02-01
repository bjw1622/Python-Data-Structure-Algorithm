class Stack:

    def __init__(self,value):
        self.array = [None] * value
        self.point = 0
        self.size = len(self.array)

    def push(self,value):
        if self.point >= self.size:
            print(f'이미 꽉 찼습니다.')
        else:
            self.array[self.point] = value
            self.point += 1

    def pop(self):
        if self.point == 0:
            print(f'pop을 수행할 값이 존재하지 않습니다.')
        else:
            print(f'팝한 데이터는 {self.array[self.point - 1]}입니다.')
            self.point -= 1

    def peak(self):
        print(f'피크한 데이터는 {self.array[self.point - 1]}입니다.')

    def find(self,value):
        find = False
        for i in range(0 , self.point):
            if self.array[i] == value:
                find = True
        if find == True:
            print(f'찾고자 하는 값은 {i}인덱스에 존재합니다.')
        else:
            print(f'찾고자하는 값은 존재하지 않습니다.')

    #나열
    def dump(self):
        for i in range(0 , self.point):
            print(self.array[i],end=" ")
        print()


st_made = Stack(10)
while True:
    print(f'현재 데이터 개수: {st_made.point} / {st_made.size}')
    next = int(input(f'(1)푸시 (2)팝 (3)피크 (4)검색 (5)덤프 (6)종료:'))

    if next == 1:
        value = int(input(f'데이터를 입력하세요:'))
        st_made.push(value)

    elif next == 2:
        st_made.pop()

    elif next == 3:
        st_made.peak()

    elif next == 4:
        value = int(input(f'검색할 값을 입력하세요:'))
        st_made.find(value)

    elif next == 5:
        st_made.dump()

    elif next == 6:
        break

    else:
        print(f'오류 발생 프로그램 종료')
        break