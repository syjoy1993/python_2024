#if

# 2 + 3
# 컴퓨터 = 기억[ram] + 연산[cpu]

# ram:변수,데이터타입,

# cpu: 연산자, 명령어():~해라,제어문
#print,input,len,연산자,변수,데이터타입[int,flaot,str,list,set,dict]

#제어문[조건문, 반복문]
#조건문 -if


# num = int(input("정수입력:"))
#
# if num > 0:  # 이거면
#     print('양의 정수 입니다.')  #이거실행
# print('프로그램 끝')
#
#
# num = int(input("정수입력:"))
# if num > 0:   # 1번
#     print('양의 정수 입니다.')
# elif num == 0:   #여러번
#     print("0 입니다")
# else:  #아니면  ///마지막
#     print("0 또는 음의 정수 입니다.")

userScore = int(input("영어점수 입력"))
if 90 <= userScore:
    print("A입니다.")
elif 80 <= userScore:
    print("B입니다.")
elif 70 <= userScore:
    print("c입니다.")
else:
    print("재수강입니다.")





num = int(input("정수를 입력"))

if num > 0:
    if num % 2 == 0:
        print("양의 짝수입니다.")
    else:
        print("양의 홀수입니다.")

elif num == 0:
    print(" 0입니다. ")

else:
    if num % 2 == 0:
        print("음의 짝수입니다.")
    else:
        print("음의 홀수입니다.")
# 쌤
#if num > 0:


# 유저에게 비밀번호 설정을 입력받고, 만약 8글자보다 작으면 비밀번호 재설정 크면 비밀번호 완료
# 나
passWord = len(input("8자리 비밀번호 설정"))

if passWord < 8:
    print("비밀번호 재설정")
else: print("비밀번호 완료")


#샘
pw = input("8자리 비밀번호 설정")

if passWord < 8:
    print("비밀번호 재설정")
else:
    print("비밀번호 완료")
#질문
# 유저에게 비밀번호 설정을 입력받고, 만약 8글자보다 작으면 비밀번호 재설정 크면 비밀번호 완료
#!가 없으면
#샘
pw = input("8자리 비밀번호 설정")
if len(pw) < 8:
    print('비밀번호가 8자리 이하 입니다')
#elif pw.count(!) ! =1:
elif '!' not in pw:
    print("특수 문자가 없습니다.")
else:
    print('비밀번호 통과')








