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