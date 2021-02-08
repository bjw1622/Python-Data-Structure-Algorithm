class Queue:

    def __init__(self,value):
        self.array = [None] * value
        self.front = 0
        self.rear = 0
        self.size = 0
        self.value = value

    def enqueue(self,value):
        if self.array[self.front] == None:
            self.array[self.front] = value
        else:
            pass
        if self.array[self.rear] == None:
            self.array[self.rear] = value
        else:
            self.rear += 1
            self.array[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.array[self.front] == None:
            print('값이 없습니다')
        else:
            print(f'{self.array[self.front]}의 값을 dequeue 하였습니다.')
            self.front += 1
        self.size -= 1

    def peak(self):
        if self.array[self.front] == None:
            print('데이터가 비어있습니다.')
        else:
            print(f'{self.array[self.front]}값이 맨 앞 데이터입니다.')

    def find(self,value):
        find = False
        for i in range(len(self.array)):
            if self.array[i] == value:
                find = True
        if find == True:
            print(f'찾고자 하는 값은 {i}인덱스에 존재합니다.')
        else:
            print(f'찾고자하는 값은 존재하지 않습니다.')

    def dump(self):
        for i in range(self.size):
            print(self.array[i],end = " ")
        print()


st_made = Queue(10)
while True:
    print(f'현재 데이터 개수: {st_made.size} / {st_made.value}')
    next = int(input(f'(1)인큐 (2)디큐 (3)피크 (4)검색 (5)덤프 (6)종료:'))

    if next == 1:
        value = int(input(f'데이터를 입력하세요:'))
        st_made.enqueue(value)

    elif next == 2:
        st_made.dequeue()

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