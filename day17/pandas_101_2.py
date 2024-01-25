import pandas as pd
from faker import Faker
faker = Faker('ko_KR')
import random
coffeeList = ['아메리카노', '라떼', '바닐라', '모카', '민초']
# data[dic] = {'name': 30명, 'age':20~60 30개, 'coffee':30}

dataDict = {
    'name': [faker.name() for i in range(30)],
    'age': [random.randint(20,61) for i in range(30)],
    'coffee': [random.choice(coffeeList) for i in range(30)]
}
df = pd.DataFrame(dataDict)
df.to_csv(f'dummy_data.csv',index=False)
#DeprecationWarning: 이거 이제 안쓸꺼에여