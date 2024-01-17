# review

#1. 리스트 컨프리헨션 을 이용한 짝수 생성
#1~20까지 숫자 중 짝수만 포함하는 리스트 생성
#
# 나
evenNum = [i for i in range(1,21) if i % 2 == 0]
#evenNum = [i for i in range(2,21,2)]
print(evenNum)

# 정답
[i for i in range(1,21) if i % 2 == 0]
evenNum = [i for i in range(2,21,2)]

#2. 조건을 포함한 리스트 컨프리헨션
# alist = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]에서 5보다 큰 숫자만 포함하는 새로운 리스트를 리스트 컴프리헨션으로 생성하세요
# 나
alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newList = [i for i in alist if i > 5]
print(newList)


#
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
overFiveList = [i for i in alist if i > 5]



#3.문자열 처리를 위한 리스트 컨프리헨션
#["apple", "banana", "cherry", "data"]에서 각 단어의 첫글자만 추출하여 새로운리스트 만들기
#
# 나
firstList = [i[0] for i in ["apple", "banana", "cherry", "data"]]
print(firstList)

#정답
fruits = ["apple", "banana", "cherry", "data"]
firstLetters = [i[0] for i in fruits]


#4.중첩된 리스트 컴플히헨션
# 1~5 숫자를 포함하는 리스트 [1, 2, 3, 4, 5]를 사용하여 각 숫자의 제곱값을 포함하는 리스트를 만드세요
num = [1, 2, 3, 4, 5]
num2 = [i**2 for i in num]
print(num2)

# 안풀음


## 6. 문자열 대문자 변환
fruits2 = ["apple", "banana", "cherry"] # 를 대문자로 변환하세요

##나

fruits2up = [i.upper() for i in fruits2]
print(fruits2up)

###정답
fruitsuppers= [i.upper() for i in fruits2]