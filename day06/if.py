#if


# 2 + 3
# 컴퓨터 = 기억[ram] + 연산[cpu]: 2 + 3 여기서 하고, 기억을 안해주면 사라짐 그래서
# 기억하라고 넣어줘야함!

# ram:변수로 데이터를 기억, 데이터타입으로 기억할 공간 확보

# cpu: 연산자, 명령어():~해라->print,input,len, 제어문

#print,input,len,연산자,변수,데이터타입[int,flaot,str,list,set,dict]

#제어문[조건문, 반복문] 코드는 위에서 아래로 시작!
# 어떤건 실행하고, 어떤건 실행 안하고 싶고, 어떤건 반복하고 싶어!
# 이걸 제어문에서 한다
# 제어문[조건문, 반복문]

#조건문 -if

num = int(input("정수입력:"))

if num > 0:  # 이거면
    print('양의 정수 입니다.')  #이거실행
print('프로그램 끝')


num = int(input("정수입력:"))
if num > 0:   # 1번
    print('양의 정수 입니다.')
elif num == 0:   #아니면 여러번
    print("0 입니다")
else:  #다아니면  ///마지막
    print("0 또는 음의 정수 입니다.")
# #유저에게 영어점수입력받고
# 100~90  A입니다
# 90~80  B입니다
# 80~70  c입니다
# 70~  재수강입니다
userScore = int(input("영어점수 입력"))
if 90 <= userScore:
    print("A입니다.")
elif 80 <= userScore:
    print("B입니다.")
elif 70 <= userScore:
    print("c입니다.")
else:
    print("재수강입니다.")

a = 10
if a > 0:
    if a < 20:
        print('a는 20 보다 작은 양의 정수 입니다.')
    else:
        print("a는 20보다 큰 양의 정수 입니다.")
else:
    if a == 0:
        print("a는 0입니다.")
    else:
        print("음수입니다.")

#유저에게 정수를 입력받고 양의 홀수, 양의 짝수, 0, 음의 홀수, 음의 짝수 출력

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
num = int(input("정수를 입력:"))

if num > 0:
    if num % 2 != 0:
        print("양의 홀수")
    else:
        print("양의 짝수")

elif num == 0:
    print(" 0입니다. ")

else:
    if num % 2 == 0:
        print("음수의 홀수")
    else:
        print("음의 짝수")


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
#만약!가 없으면 특수문자가 없습니다.
#다 통과 된다면 비밀번호 완료


# #나
# passWord = len(input("8자리 비밀번호 설정"))
# #print(passWord)  이값이 8이기 때문에 안됌
#
# if passWord < 8:
#     print("비밀번호가 8글자 이하 입니다")
# elif "!" not in passWord:
#     print("특수문자가 없습니다")
#
# else: print("비밀번호 완료")
#





#샘
pw = input("8자리 비밀번호 설정")
if len(pw) < 8:
    print('비밀번호가 8자리 이하 입니다')
#elif pw.count('!') != 1:    pw안에 !가 1개가 아니라면
elif '!' not in pw:  # pw에! 가 없네요
    print("특수 문자가 없습니다.")
else:
    print('비밀번호 통과')








