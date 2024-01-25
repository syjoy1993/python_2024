import pandas as pd

df = pd.read_csv('dummy_data.csv')
print(df[df['coffee'] == '바닐라'][df['age'] > 30]) # 바닐라 러버 40대이상

# 데이터 프레임 함수

#위에서 10개/ 뒤에서 10개
print(df.head(10))
print(df.tail(10))

# 데이터 요약본, 양,평균,표준분포 ,최소, 최대
print(df.describe())

#  age
# count  30.000000
# mean   37.233333
# std    11.230142
# min    22.000000
# 25%    29.000000
# 50%    36.000000
# 75%    43.750000
# max    61.000000

# 이름 기준 정렬
print(df.sort_values(by='name'))
#나이기준으로 정렬
print(df.sort_values(by='age'))
# 커피 순으로 정렬
print(df.sort_values(by='coffee')) #

# 데이터 변경 및 조작
df['age'] = df['age'] // 10 #몫으로 변화 -> 30대 20대 0   임예준    5    바닐라
print(df)

# groupby 데이터 특정 기준으로 그륩화
groupedCoffee = df.groupby('coffee')
print(list(groupedCoffee))