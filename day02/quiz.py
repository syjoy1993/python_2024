

# # 태어난 연도 입력, 현재 만나이 출력하는 프로그램
# # EX 2000 -> 23
# # 세개의 숫자를 입력받고 총합, 평균 (실수) 출력
#
# year = int(input("태어난 연도 입력"))
# Y = 2024
# print(f"현재 만나이는{Y - year}")
#
# a = float(input("숫자1"))
# b = float(input("숫자2"))
# c = float(input("숫자3"))
# d = print(f"{a + b + c}")
# print(f"{}")
# userYear = int(input("몇년생이십니까:"))
# print(f"귀하의 나이는 만 {2024 - userYear - 1}입니다.")
#
# a = float(input("숫자1"))
# b = float(input("숫자2"))
# c = float(input("숫자3"))
# sum = a+b+c
# avg = (a+b+c)/3
# print(f"총합: {sum}, 평균:{avg}")

#3 섭씨 온도를 입력받아 화씨 온도로 변환을 출혁하는 프로그램만들기
# F=C*5.9+32입니다.

C = float(input("현재 섭씨온도를 입력하세요."))
F = C * 5.9 + 32
print(f"현재 섭씨는 화씨로 {F} 입니다.")


#답
#cel = float(input("섭씨온도를 입력하세요."))
#fah = cel * 5.9 + 32
# 변수[실수]:.2f 둘째자리출력


#4 사용자의 키(m)와 몸무게(kg)를 입력받아 bmi을 출력하는 프로그램을 만들기
# bmi = 무게/키**2
heigh = float(input("당신의 키를 입력하세요"))
weight = float(input("당신의 몸무게를 입력하세요"))
bmi = weight / (heigh ** 2)
print(f"당신의 bmi는 {bmi:.2f}입니다.")

#5 반지름 입력시 원의 넓이와 둘레를 구하는 프로그램
r = float(input("반지름을 입력하세요.")) #int도 가능
extend = 3.14 * r ** 2
circumF = 2 * 3.14 * r
print(f"원의 넓이:{extend} 원의 둘레: {circumF}")


#총정리
# print() - 출력
# input() - 입력 [결과 :문자 타입]
# 변수 -임시 저장하는곳
#int() / float() /str()
#사칙연산 +-* /나누기 %나머지 //몫 **제곱