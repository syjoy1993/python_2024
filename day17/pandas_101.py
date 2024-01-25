import pandas as pd
# dataframe

data = {
    'age': [30, 40, 50, 40, 50],
    'name': ['a', 'b', 'c', 'd', 'e'],
    'gender': ['m', 'f', 'f', 'm', 'm']
}
df = pd.DataFrame(data) # 데이터 프레임이라는 클래스, 변수 data
# class = 변수 + 함수
# shape : 행과 열의 수를 돌려줌
# dataFrame = 변수
print(df)
print(df.shape)
# 출력(5, 2)

#index 행
print(df.index)
#column 열
print(df.columns)
#values 데이터 [list] 전부다!
print((df.values)) # 배열이다 == print((df.values[0])) 과 한줄이 같음!
# 해당열 뽑기
print(df['age']) # age열 전부
# 0    30
# 1    40
# 2    50
# 3    40
# 4    50
print(df[['age', 'name']]) # 두개 열 뽑기!

# 해당 열 뽑기 + 조건
print(df[df['age'] > 30]) # 30이상인 애들 뽑아주세여
print(df[df['gender'] == 'f'])
#print(df[df['age'] > 40 and df['gender'] == 'f'])
# and연산자 안먹힌다
fdf40 = df[df['age'] > 40][df['gender'] == 'f']

# 행 뽑기
print(df.loc[0])
print(df.loc[0,'name']) # a


