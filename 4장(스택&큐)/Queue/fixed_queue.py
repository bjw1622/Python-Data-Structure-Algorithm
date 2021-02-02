from typing import Any

class FixedQueue:

    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self,capacity):
        self.no = 0 #현재 데이터 개수
        self.front = 0
        self.rear = 0
        self.capacity = capacity #큐의 크기
        self.que = [None] * capacity #큐의 본체

    def __len__(self):
        #큐에 있는 모든 데이터 개수를 반환
        return self.no

    def is_empty(self):
        #큐가 비어있는지 판단
        return self.no <= 0

    def is_full(self):
        #큐가 꽉 찾는지 판단단
        return self.no >= self.capacity

    def enqueue(self,x):
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1

        #rear가 크기랑 같으면 다시 rear을 0으로해서  다시 채우기
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self):
        if self.is_empty():
            raise FixedQueue.Empty

        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front
        return x

    def peek(self):
        if self.is_empty():
            return FixedQueue.Empty
        return self.que[self.front]

    def clear(self):
        self.no = self.front = self.rear = 0

    def find(self,value):
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1

    def count(self,value):
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[i] == value:
                c += 1
        return c

    def __contains__(self, value):
        return self.count(value)

    def dump(self):
        if self.is_empty():
            print('큐가 비어 있습니다')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end="")
            print()