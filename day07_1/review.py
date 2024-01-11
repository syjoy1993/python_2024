# 홀수 짝수 확인

num = int(input("숫자 하나 입력"))

if num % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")

#e답
number = int(input("숫자 하나 입력"))

if number % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")

#알파벳탐지기 문자 하나 입력 ,알파벳이라면 '알파벳입니다'그렇지 않으면 '알파벳이 아니에요

alpha = input("문자 하나 입력")  # input 자체는 스트링
if alpha in
    print("알파벳 입니다")
else:
    print("알파벳입니다")



#답
alpha = input("문자 하나 입력")  # input 자체는 스트링
if alpha.isalpha():  #알파벳인지 확인 할 수있는기능 T or F  새로운 기능 추가, 기능변화 자주 있음
    print("알파벳 입니다")
else:
    print("알파벳이 아닙니다")

#비밀번호 설정
#최소 10글자 이상 틀리면 최소 10글자설ㅈㅓㅇ해주세요
# 영어와 숫자의 조합필요
# 특수문자 반드시 하나 포함 !@#$

pw = input("!@#$포함한 영문 숫자 조합 10자리 비밀번호 입력")

if len(pw) >= 10:
    if pw in


else:
    print("최소 10글자 이상 설정해주세요")



# #답
password = input("비밀번호 설정")
# if len(password) < 10:  #len 파이썬 내장된 기능
#     print("최소 10글자 이상 설정하세요!")
#
# elif password.isalnum() or ('!' in password or '#' in password or '@' in password) :   #이거??무엇? 숫자랑 영어 있나?
#     print("영어와 숫자를 꼭 포함해주세요")
# else:
#     if not ('!' in password or '#' in password or '@' in password):
#         print("특수문자를 !@# 포함해주세요")
#     else:
#         print("비밀번호 설정 완료")
#
#
# 버스요금계산
# 시내버스 1200
# 광역버스 2000
# 마을 버스 1000

# 연령별 할인률
# 7세이하 무료
# 8~19 30%할인
# 65이상 무료
#
# 사용자의 나이와 선택한 노선에 따라 할인을 적용한 버스요금을 계산 하여 출력

busUser = {
    busSort:['시내버스','광역버스','마을버스'],
    busPrice:['1200','2000','1000'],
    user:['어린이','청소년','노인'],
    discount:[0,0.7,0]
}

input("버스 노선을 고르세요")

# #답
# bus = {
#     1: {
#         'name': '시내버스',
#         'price': 1200,
#     },
#     2: {
#         'name': '광역버스',
#         'price': 2000,
#     },
#     3: {
#         'name': '마을버스',
#         'price': 1000,
#     },
# }
#
# bus_choice = int(input(f"버스를 선택하세요[!.시내버스 -1200, 2.광역버스 - 2000원, 3.마을버스- 1000] "))
# age = int(input("나이를 입력하세요!"))
#
# if age <= 7 or 65 <= age:
#     print("무료입니다!")
# elif 8 <= age and age <= 19:
#     print(f"{bus[bus_choice]['name']}의 {{bus[bus_choice]['price']*0.7}")
# else:
#     print(f"{bus[bus_choice]['name']}의 {{bus[bus_choice]['price']}")
#