#02 산술연산자 +,-,*,/,//,%.** 배움  결과가 실수안에 닫혀있다

# 100이하의 정수를 입력받고 10의 자리와 1의 자리를 출력하는 프로그램
# ex) 89 -> 8,9

# a = int(input("100이하의 정수 입력"))
#listA = list(a)
#print(listA [1][0])

#정답
num = int(input("정수 입력:"))
ten = num // 10 #7
one = num % 10 #5

#1000이하의 정수를 입력받고  분과 시로 환산하는 프로그램
num = int(input("1000이하의 정수 입력:"))
time = num // 60
min = num % 60
print(f"시간은 {time}시 {min}분")
#정답
# time = int(input("1000이하의 정수 입력:"))
# min = num // 60
# sec = num % 60
# print(f"시간은 {min}시 {sec}분")

#드래그 + ctrl+ /

#정수: 10000~99999 사이를 입력받고 100의 자리 값을 출력하는 프로그램
# num = 10000< int(input("10000<정수 입력<99999:"))< 99999
# num_list = list(num)
# print(num_list[2])
num = int(input("10000~99999 사이의 정수"))
#45687 -> 456 아래 식
hundred = num // 100
result = hundred % 10

#비교연산자 >, <, >=(이상), <=(이하),숫자만 타켓// ==(같다), !=(다르다) 숫자+문자까지
#결과가 불린값에 닫혀있다.=> ture or false
#결과 :bool

print(3 < 1)
print(3 > 1)

a = 3 > 1 #bool type
b = 3 == 1 #bool type [False]
c = 3 !=1 #bool type [true]


#논리연산자 [결과: bool] 결과는 bool타입에 닫혀있다, 타겟도 bool
#and : 피연산자가 모두 true이면 ture 예시에서 3 > 1,5 > 1
print(3 > 1 and 5 > 1) #Ture
#or : 피연산자가 하나라도 Ture이면 ture
print(5 < 1 or 3 < 1 or 0 < 1 )

#not : false -> true , true -> false
print(not(3 > 1)) #true -> false

#할당 연산자
a = 1 #할당연산자 =
a = 3 #3으로 갈아치우기
# a얼마??? 3
#b = b + 3 #3을 더해주기
b += 3 #3을 더해주기 축약.ver
b -= 3 # 3을 빼주기
b *= 3 #3을 곱해주기
b /= 3 #3을 나누기해주기



