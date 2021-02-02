class FixedStack:
    #고정 길이 스택 클래스

    #비어있는 상태에서 pop
    class Empty(Exception):
        pass
    #꽉 찬 상태에서 push
    class Full(Exception):
        pass

    def __init__(self,capacity):
        self.stk = [None] * capacity     #스택 본체
        self.capacity = capacity         #스택의 크기
        self.ptr = 0                     #스택 포인터

    #스택에 쌓여있는 갯수 반환
    def __len__(self):
        return self.ptr

    def is_empty(self):
        return self.ptr <= 0

    def is_full(self):
        return self.ptr >= self.capacity

    def push(self,value):
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self):
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self):
        if self.is_empty():
            return FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self):
        self.ptr =  0

    def find(self,value):
        for i in range(self.ptr - 1 ,-1 , -1):
            if self.stk[i] == value:
                return i
        return -1

    def count(self,value):
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c

    def __contains__(self, value):
        return self.count(value)

    def dump(self):
        if self.is_empty():
            print('스택이 비어 있습니다')
        else:
            print(self.stk[:self.ptr])