# DataStructure&Algorithm
## 1장(알고리즘 기초)

    알고리즘이란
  
    -> 어떠한 문제를 해결하기 위해 정해 놓은 일련의 절차
    
    복잡도란?
    
    -> 복잡도. (점근 표기법 : Big-O Notation)
           O(1) : 입력 자료의 수에 관계없이 일정한 실행 시간을 갖는 알고리즘
           O(log N) : 입력 자료의 크기가 N일경우 log2N 번만큼의 수행시간을 가진다.
           O(N) : 입력 자료의 크기가 N일경우 N 번만큼의 수행시간을 가진다.
           O(N log N) : 입력 자료의 크기가 N일경우 N*(log2N) 번만큼의 수행시간을 가진다.
           O(N2) : 입력 자료의 크기가 N일경우 N2 번만큼의 수행시간을 가진다.
           O(N3) : 입력 자료의 크기가 N일경우 N3 번만큼의 수행시간을 가진다.
           O(2n) : 입력 자료의 크기가 N일경우 2N 번만큼의 수행시간을 가진다.
           O(n!) : 입력 자료의 크기가 N일경우 n*(n-1)*(n-2)... * 1(n!) 번만큼의 수행시간을 가진다. ex)외판원 문제(TSP)의 기본적인 해법

       
        순차구조:한 문장씩 처리 되는 구조

        선택구조:조건식으로 평가한 결과에 따라 프로그램의 실행 흐름이 변경되는 구조

        for _ in range  => _를 이용하여 무시하고 싶은 값을 표현 할 때
        
        import radnom => random.randint(a,b) a이상 b이하 무작위 난수 


## 2장(기본 자료구조와 배열)

    자료구조란?
    
    -> 데이터 단위와 데이터 자체 사이의 물리적 또는 논리적인 관계 , "논리적인 관계로 이루어진 데이터 구성"
       즉 데이터가 모여 있는 구조이며 많은 데이터를 모아 효율적으로 관리하고 구조화 가능하다.
    
    
    배열이란?
    
    -> 리스트와 튜플로(데이터 컨테이너) 구현 , 변수를 하나로 묶어서 사용할 수 있어 코드를 쉽고 효율적으로 작성 가능
    
    내포 표기 생성이란?
    
    -> 리스트 명 = [표현식 for 변수 in 반복 가능한 대상 if 조건문]

    등가성과 동일성에 대해
    
    -> 두 객체의 값이 같은지 비교는 == 등가성
       두 객체의 값과 식별 번호가 같은지 is 동일성
       
    재사용할 수 있는 모듈 작성하기
    
    if __name__ == "__main__": => 직접 main파일을 시작했을 경우에만 실행되는 조건!
    
    for i, x in enumerate(리스트): =>인덱스와 원소를 짝지어 튜플로 꺼내는 
    
    얇은 복사: x.copy() => 참조하는 곳 까지 복사 , 수정해도 같은 값 유지 , 참조값만 복사
    
    깊은 복사:copy.deepcopy(x) => 객체가 갖는 모든 멤버를 복사
    
    
## 3장(검색 알고리즘)
    
    검색 알고리즘이란?
    
    ->데이터 집합에서 원하는 값을 가진 요소를 찾아내는 알고리즘 대표적으로 선형 검색, 이진 검색, 해시법
    
    선택할 수 있는 알고리즘이 다양한 경우에는 용도, 목적, 실행 속도, 자료구조 등 여러 사항을 고려해서 선택한다.
    
    
    선형 검색이란?
    
    ->무작위로 늘어놓은 데이터 집합에서 검색을 수행
    
        선형 검색의 종료 조건:
            1) if i == len(a):
            2) if a[i] == key:
        
        보초법 
        
        ->선형 검색을 통해 찾은 값이 기존의 배열에 존재하는 데이터인지 또는 보초로 설정해둔 특정의 값인지 구별만 할 수 있도록 코드를 
          작성하여 선형 검색 알고리즘의 종료 조건을 검사하는 비용을 50%나 줄일 수 있어 더욱 효율적인 방법

    
    이진 검색이란?
    
    ->일정한 규칙(정렬)으로 늘어놓은 데이터 집합에서 아주 빠른 검색을 수행
        
        pl(맨 앞 인덱스) = 0
        pr(맨 뒤 인덱스) = n -1
        pc(중간 인덱스) = (n-1) // 2
        
        이진 검색에서 검색 범위를 좁히는 과정

            1)a[pc] < key: 중앙에서 오른쪽으로 한 칸 이동하여 새로운 왼쪽 끝 pl로 지정하고, 검색 범위를 뒤쪽 절반으로 좁힌다.
            2)a[pc] > key: 중앙에서 왼쪽으로 한 칸 이동하여 새로운 오른쪽 끝 pr로 지정하고, 검색 범위를 앞쪽 절반으로 줄인다.
        
        이진 검색의 종료 조건
        
            1)a[pc]와 key가 일치하는 경우
            2)검색 범위가 더 이상 없는 경우
            
        index() 함수로 검색하기
        
            리스트 or 튜플에서 검색은 index 함수로 실행가능.
            가장 가까이 있는 값 반환
            ex)리스트명.index(찾고자하는 값)
            ex)리스트명.index(찾고자하는 값,시작 범위 설정)
            ex)리스트명.index(찾고자하는 값,시작 범위 설정,끝 범위 설정)
    
    해시법이란?
         
         데이터를 저장할 위치 = 인덱스 를 간단한 연산으로 구하는 것
        ->추가, 삭제가 자주 일어나는 데이터 집합에서 아주 빠른 검색을 수행

    해시함수: 키를 해시값으로 변환하는 과정
    
    해시법에 충돌을 해결 하는 방법
        
        -체인법:같은 해시값 데이터를 연결 리스트로 연결하는 방법
        -오픈 주소법: 데이터를 위한 해시값이 충돌할 때 재해시하는 방법

    해시 함수 구하는 방법
        
        -key가 int형인 경우: key를 해시의 크기 capacity로 나눈 나머지
        -key가 int형이 아닌 경우: 표준라이브러리를 이용하여 형변환
        
        
## 4장(스택과 큐)
    스택이란?
       
    =>데이터를 임시 저장할 때 사용하는 자료구조로, 데이터의 입력과 출련 순서는 후입선출(가장 나중에 넣은 데이터를 가장 먼저 꺼낸다)(LIFO)방식 입니다.
    
    Push:스택에 데이터를 넣는 작업
    Pop: 스택에서 데이터를 꺼내는 작업 
    Top:꼭대기
    Bottom:바닥
    
~07.15
js로 알고리즘
