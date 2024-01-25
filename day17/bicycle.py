import pandas as pd

df = pd.read_csv('bicycle.csv', encoding='cp949')
startList = df['시작_대여소명'].tolist()  #tolist() 리스트화
# 00동 몇명 _이하는 삭제
a = '불광2동_021_1'.split('_')
print(a) #['불광2동', '021', '1']
b = '불광2동_021_1'.split('_')[0]
print(b) #불광2동
places = {}

for i in startList:
    dong = i.split('_')[0]
    if dong in places:
        places[dong] += 1
    else:
        places[dong] = 1



# 아침 점심 저녁 새벽으로 나누고, 동과의 상관관계



