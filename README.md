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
    
