# 1. 핸드폰번호 가리기
#
# phone_number = ''
def solution(phone_number):
    masking_num = ""
    for index,i in enumerate(phone_number):
        if index > 0:
            masking_num += i
        else:
            masking_num += '*'

    return masking_num
a = solution("01024019304")
print(a)



# 2.영어 ㄴㄴ
# 영어입력을 숫자로
# 내일 품!
# numbers 매개 변수
# "onetwothree" =>123

def solutionA(numbers):
    number_name = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers_dic = {index + 1: i for index, i in enumerate(number_name)}
    numbering = ''
    # if numbers in numbers_dic:
    #     numbering += numbers_dic[]





