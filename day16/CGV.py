import pandas as pd
import random
from faker import Faker
from datetime import *

fake = Faker('ko_KR')

movieList = ['웡카', '시민덕희', '도그맨', '너의 이름은', '라라랜드', '상견니', '외계인']
snackList = ['일반팝콘', '캬라멜 팝콘', '치즈팝콘', '구운오징어', '나쵸', '프레즐', '핫도그']
drinkList = ['콜라', '제로콜라', '스프라이트', '환타', '에이드', '물']

#cgvData 일일 손님 매출 데이터
cgvData = {
    'customers': [fake.name() for i in range(500)],
    'movies': [random.choice(movieList) for i in range(500)],
    'snack': [random.choice(snackList) for i in range(500)],
    'drink': [random.choice(drinkList) for i in range(500)]
}
now = datetime.now()
cgv_df = pd.DataFrame(cgvData)
cgv_df.to_csv(f'0124cgv.csv',index=False)
