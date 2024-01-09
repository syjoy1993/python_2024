#list_advance

#리스트 연산자
# 더하기 연산자
# +: int + int (사칙연산)
# +: str + str (문자연결연산)
# +: list +list(리스트 연결 연산)
coffee = ['아메리카노', '라떼','바닐라라떼']
cookie = ['화이트쿠키','녹차쿠키','오레오쿠키']
menu = coffee + cookie
print(menu)

# 곱하기 연산자 = 반복
# int * int (사칙연산)
# str * int (str을 n번 반복)
# list * int (list를 n번 반복)
double_menu = menu * 2
print(double_menu)


#  in 연산자 : boolean 타입으로 변환
print('아메리카노' not in menu)
print('디카페인' not in menu)

# slicing [:] 슬라이싱 연산자:
newMenu = menu[0:3]
print(newMenu)
# [0],[1] 출력한다.
newMenu = menu[:2]
print(newMenu)
#['아메리카노', '라떼'] 처음부터 n번까지 출력함

newMenu = menu[1:]
print(newMenu)
#['라떼', '바닐라라떼', '화이트쿠키', '녹차쿠키', '오레오쿠키'] 마지막까지 출력함

