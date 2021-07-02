list01 = list([1,2,3])
list02 = list(range(1,5))
list03 = list(range(1,5,3))
list04 = list(["A","B",'C'])


tuple01 = tuple((1,))
tuple02 = tuple((1,23,231))


print(list01)
print(list02)
print(list03)
print(list04)

print(tuple01)
print(tuple02)

#언팩

x = [1,2,3]
a,b,c = x
print(a,b,c)

#내포 표기 생성
numbers = [1,2,3,4,5]
twise = [num * 2 for num in numbers if num % 2 == 1]
print(twise)
#리스트 명 = [표현식 for 변수 in 반복 가능한 대상 if 조건문]
meter_list = [3,7,9,10]
c_list = [i*100 for i in meter_list if i % 2 != 0]
print(c_list)

#등가성과 동일성에대해
#두 객체의 값이 같은지 비교는 == 등가성
#두 객체의 값과 식별 번호가 같은지 is 동일성