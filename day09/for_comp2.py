# #for 컨프리헨션 조건문

###1. if가 뒤에 있을때는 filter 컷 역할

## [i for in  range(1,101)] 1~100
#[i for in  range(1,101) if i % 5 == 0]

fruits = ['apple', 'strawberry','mango','orange','melon']

a = [i for i in fruits if i.count('a') > 0] #'a'하나 이상 포함 리스트
b = [i for i in fruits if i.count('r') == 1] #r이 하나만 포함
# 글자수가 6글자
c= [i for i in fruits if len(i) >= 6] # 6글자 이상인 단어들 ['strawberry', 'orange']

### 2. if -else 있을 떄는 map 변환/치환 역할

#[for i in range(1,101)]#1~100
ia = ['🍓'if i % 2 == 0 else i for i in range(1,101)]
#만약에   i % 2 == 0이면 '🍓' 아니면 i를 주세요
print(ia)


# 유저에게 n을 입력받고 1~100까지 리스트를 출력하는데, n의 배수만 당근을 표현해주고 나머지는 숫자로
num = int(input("정수입력"))

carrot= ['🥕'if i == num * 2 else i for i in range(1,101) ]
carrot= ['🥕'if i % n == 0 * 2 else i for i in range(1,101) ]

#답
num = int(input("정수입력"))


# fruits = ['apple', 'strawberry','mango','orange','melon'] 에서 5글자 이하이면 대문자로 바꿔서 출력하고 아니면 토끼로 출력하는 리스트만들기
rabit = [i.upper() if len(i) <= 5 else '🐇'for i in fruits]

#답
rabit = [i.upper() if len(i) <= 5 else '🐇'for i in fruits]


## for 컴프리헨션 중첩 루프문

h =[i*j for i in range(1,3) for j in range(1,4)]
# i-1 j-123
# i-2 j-123
# i-3 j-123

g = [i for i in ["apple", "banana"] for j in ["pie","tnaghuru"]]
print(g)
