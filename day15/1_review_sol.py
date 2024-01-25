# 1. 핸드폰번호 가리기
#

def solution(phone_number):
    newNumber = ""
    for index,item in enumerate(phone_number):
        if len(phone_number) - 4 > index:
            #어떤 번호 길이던 4자 뒤에는 제외됌
            newNumber += "*"
        else:
            newNumber += item
    return newNumber
a = solution("01023345678")
print(a)



# 2.영어 ㄴㄴ
# 영어입력을 숫자로
# 내일 품!