from __future__ import annotations
from typing import Any,Type
import hashlib

class Node:
    #해시를 구성하는 노드

    def __init__(self, key, value, next):
        self.key = key #키
        self.value = value # 값
        self.next = next #뒤쪽 노드 참조

class ChainedHash:
    #체인법으로 해시 클래스 구현

    def __init__(self,capacity):
        self.capacity = capacity #해시 테이블의 크기를 지정
        self.table = [None] * self.capacity # 해시 테이블 리스트 선언

    def hash_value(self,key):
        #해시값 구하기
        if isinstance(key,int):     #key가 int형일때
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(),16) % self.capacity)     #key가 int형이 아닐때 형변환을 위해서 라이브러리 사용

    def search(self,key):
        #1.key 값을 해시함수를 이용해 해시값으로 반환
        #2.해시값을 index로 하는 배열 주목
        #3.배열의 링크드리스트를 맨 앞부터 하나씩 검색

        hash = self.hash_value(key)     #검색하는 키의 해시값,형변환완료
        p = self.table[hash]            #찾고자하는 노드

        while p is not None:
            if p.key == key: #우리가 찾고자하는 키값이랑 같으면
                return p.value
            p = p.next

        return None

    def add(self,key,value):
    #키가 key이고 값이 value인 원소를 추가
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False #key가 이미 등록된 경우면 실패
            p = p.next       #뒤쪽 노드 계속 확인

        temp = Node(key,value,self.table[hash])
        self.table[hash] = temp      #노드를 추가
        return True                  #추가 성공

    def remove(self,key):
        hash = self.hash_value(key) #검색하고자하는 key 형변환
        p = self.table[hash]  #노드를 주목
        pp = None #바로 앞의 노드 주목

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True #key 삭제
            pp = p
            p = p.next #뒤쪽 노드 주목
        return False #삭제 실패

    def dump(self):
        for i in range(self.capacity):
            p = self.table[i]
            print(i,end="")
            while p is not None:
                print(f' -> {p.key} ({p.value})',end="")
                p = p.next
            print()












