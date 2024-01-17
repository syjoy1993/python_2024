# funtion
# 함수
# 코드를 모아놓은 묶음들
# 수학적 함수랑 같다
# f(x)  = x + 10  input =>  코드를 모아놓은 묶음들 => output
# input 없는데 output 있을수도 있고, 반대일수도 잇다.


###파이썬 내장함수, 파이썬 설치하면 기본으로 있움!
# print(input) # 프린트 함수
# input(input) # 인풋함수
# int(input) # 정수화 함수
# enumerate(input) # 인덱스와 값을 보여주는 함수

## ????() 함수의 모양

## 파이썬 커스터마이즈 함수

def add(x,y):
    result = x + y
    return result
a = add(5,6)
print(a)


#minus 함수만들기
def minus(x,y):
    return x - y

 # result = x - y
 #return result 를 축약해서

 #return x - y가능


b = minus(99,50)
print(b)


#multiply 함수만들기
def multiply(x,y):
    return x * y  # 숫자형을 돌려줌

c = multiply(5,5)
print(c)

# 어떤 숫자 num 홀수면 홀수입니다. 짝수이면 짝수입니다. 돌려주는 함수

def isEvenNum(x):
    if x % 2 == 0:
        return "짝수입니다."
    else:
        return "홀수입니다."

print(isEvenNum(2344))

#답
def oddEven(x):
    if x % 2 == 0:
        return "짝수입니다."
    else:
        return "홀수입니다." # 문자열을 돌려줌

#
# print("화요일")
# print("화요일") 의 돌려주는값? none type
# 단지 콘솔에 찍고 돌려주는것은없는것

# def oddEven2(x):
#     if x % 2 == 0:
#         return print("화요일")
#     else:
#         return "홀수입니다." # 문자열을 돌려줌
#
# a = oddEven2(5)
# print(a)  # print("화요일") 의 돌려주는값? none type 에러뜸


# 매개변수 리스트 2개를 받고 그거를 딕셔너리 화 해서 돌려주는 함수를 만들어보기


