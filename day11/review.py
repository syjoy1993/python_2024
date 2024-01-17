# review
#1.리스트 컴프리헨션 필터링
# 리스트에서 5보다 크고 문자'a'를포함하는 문자열만

words = ["apple", "banana", "cherry", "data","elderberry","fig"]
newWords = [i for i in words if len(i) > 5 and i.count('a') > 0]

newWords = [i for i in words if 'a' in i and len(i) > 5]

print(newWords)

#@리스트 50보다 큰 숫자
numbers = [30, 55, 20, 75, 40, 90, 10, 65]

newNum = [i for i in numbers if i > 50 ]

print(newNum)
#3 두 정수의 덧셈 뺄셈
# 두정수 a,b bool변수 flag

def plusOrMinius(a,b,flag):
    if flag == True:    #flag: 로 축약 가능
       return  a + b
    else:
        return a - b
