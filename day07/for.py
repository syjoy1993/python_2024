# # print, input, 변수, 데이터타입 [int,float,str,bool,list,set,dict]
# import random
#
# #if random 연산자
#
# #컴=기억+연산
# # ram: 변수[데이터타입],random
# # cpu: 연산자, 명령문[print(), input(), len(), bool()...], 조건문[if], 반복문[for]:~여러번 반복
#
for x in range(10):            #기본방법, x는 미지수 range 0~9까지
    print(x)
print("끝")

# # num = int(input("몇번까지 보실래요?"))
# # for x in range(num + 1):
# #     print(x)
# # print("끝")
# #둘중 하나 사용
num = int(input("몇번까지 보실래요?")) +1
for x in range(num):
    print(x)
print("끝")
# #
# #
num = int(input("몇번까지 보실래요?")) +1
for x in range(num):
    if x % 2 == 0:
        print(x)
print("끝")

# # #정수 입력받고, 해당 수의 공배수
#
num = int(input("공배수입력?"))
for x in range(100):
    if x % num == 0:
        print(x)
print("끝")


# # 1~10까지 더하는 프로그램
sum = 0
for x in range(11):
    sum += x
print(sum)

# #유저에세 몇번째까지의 정수를 받고 , m의 정수를 받으면
# #0~n까지 m의 공배수의 총합

# userN = int(input("몇번 입력"))
# x = int(input("숫자 입력"))
#
# for x in range(userN):
#     sum
#     x = x * userN
# print(sum)

#답
# n = int(input("몇번째까지")) + 1


#다음시간

#0~10000까지 랜덤한 숫자를 담고 있는 6개의 정수를 담고 있는 list출력

# import random
#
# A = random.randint(0,10000)
#
# for x in range (7):
#      random.randint(0, 10000):
#     print("x")
#
# print(list(numList))