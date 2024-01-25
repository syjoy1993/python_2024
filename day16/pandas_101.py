# pandas
# 엑셀을 파이썬화, 엑셀 상위 호환
# 알고리즘에서 중요한것 - 데이터 타입!
# 판다스에서 만든 데이터 타입 2개
# series, dataframe 두개가 있다
# series: 엑셀에서 하나의 열
# dataframe: 엑셀 그 자체[스프레드 시트 ]= 압도적으로 많이 사용함

import pandas as pd
# 별명붙여주자 pd
from faker import Faker
numList = [5, 12, 24, 13, 17]
series = pd.Series(numList) #pd에 있눈 Serises데이터화 할게/ 데이터 타입 시리즈임
#그리고 새로운 변수에 넣어줄게
print(series)
#series.여러가지 나옴
#mean 평균
print(series.mean)


# coffee = ['banapresso', 'starbucks', 'coffeebean', '아마스빈', '팔공티']
# coffeeserises = pd.Series(coffee)  #데이터 타입은 시리즈
# print(coffeeserises)
#

#데이터프레임 dataFlame 딕셔너리로 넣어줘야함
coffeedata = {
    "menu": ['amerocano', 'latte', 'mocha', 'vanilla', 'mint'],
    "price": [2500, 3000, 3500, 3500, 4000],
    "caffein": [120, 100, 80, 100, 50]

}

df = pd.DataFrame(coffeedata)
print(df)

df.to_csv('coffee.csv', index=False)
# to_csv :엑셀파일로 만들어줌, (이름은 이렇게 해주고,인덱스는 빼고 해조)

#지금부터 faker를 쓸꺼야, faker를 받아와서 import 함
#faker라이브러리는 자기가 알아서 이름을 만들어 줌
# fake = Faker() 영어이름
fake = Faker('ko_KR') #한국어 이름
# print(fake.name()) # 실행 할 때마다 임의 이름이 만들어짐

carData = {
    'carName': ['k5', 'k7', 'avante', 'k3', 'tesla'],
    'onwer':[fake.name() for i in range(5)],   #range(5) 5번 돌려주라 fake.name()을
}

df2 = pd.DataFrame(carData)
df2.to_csv('car.csv',index=False) #한글 깨지면 한셀쓰거나, 엑셀 설정을 바꾸면됌