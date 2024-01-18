#map  filter

#1. map -변경/ 치환해주는 함수

# numList = [1,2,3,4,5]
# a = map(lambda x: x**2,numList)
# b = map(lambda x: x+100,numList)
# print(b)
#
# c = map(lambda x: x**2+100,numList)

coffeepriceList = [2000, 3000, 3500, 4000]
# 각각 +1000 ,+원

d = list(map(lambda x: str(x+1000)+'원', coffeepriceList))
print(d)

fruits = ['apple', 'banana', 'mango', 'avocado']

e = map(lambda x: len(x),fruits)


# filter(어떻게, 무엇을) 컷, 필터 걸러준당

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter(lambda  x:x > 5,numList)

f = list(filter(lambda x: x % 2 == 0,numList))
print(f)

g = list(filter(lambda x: x.count('o')>0,fruits))
print(g)

#문자 길이가 6글자 있는에만 주고 +'😺banana'
h = print(list(map(lambda x:'😺'+x, filter(lambda x: len(x)>5,fruits))))
