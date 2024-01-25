#"onetwothreefourfivesixseveneightnine"

def solution(numbers):
    numList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for index, item in enumerate(numList):
        numbers = numbers.replace(item,str(index))
        #넘버스가 영어로되있는 숫자인ㄷ 애를 그 아이템의 인덱스를 스트링화 해서 바꿔주세요. 넘버스를 바꺼줘
    return int(numbers)
print(solution("onetwothreefive"))
