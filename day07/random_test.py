# random _test


import random # ramdom을 가져올게~
print(random.randint(0,100))  #.누르먄 기능 나옴  ,,,
# -> 랜덤으로 숫자를 뽑으게요 0~100까지 실행할떄마다 랜덤

print(random.random())  # 0~1 사이 실수! 중에 암거나 표준분포,,,

fruits = ['사과','망고','바나나', '멜론']
print(random.choice(fruits))  # 후르츠에서 암거나 뽑아줘

random.shuffle(fruits)  #리스트를 넣었을 때 랜덤으로섞어요
print(fruits)
#위에 4개 주로 많이 사용