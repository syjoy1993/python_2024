#dataType

first = input("첫번째 수:")
#firstN = '1'

second = input("두번째 수:")
#secondN = '2'
#result = '12'
print(f"{first + second}")

#input 은 무엇을 넣을지 모르기 때문에 문자로 취급한다.
#input() : 유저 힌테 입력받는 기능
#print(): 안에들어 있는 내용을 출력
# int(): 안에 들어 있는 문자를 정수화

first = input("첫번째 수:")
#여기 까지는 문자
int_first = int(first)
#문자를 받아서 정수화
second = input("두번째 수:")
int_second = int(second)
print(f"{int_first + int_second}")

#축약ver
first = int(input("첫번째 수:"))
second = int(input("두번째 수:"))
print(f"합: {first + second}")
print(f"곱: {first * second}")
print(f"차: {first - second}")

a = 10 # a는 숫자 정수형 타입
b = 3.14 # b는 숫자 실수형 타입
c = "megastudy" # c는 문자형 타입

# cpu[연산] + ram[기억]
a = 10 # (=)대입 연산자
b = 3.14




