# standard_modules : 기본적으로 깔려져있는아이들
import random # 랜덤기능쓰기
random.randint

# 난 randint이놈만 쓸꺼야!

# from random import randint
# randint

# 랜덤기능 전부쓸꺼야

from random import *
randint
randbytes






# random: 랜덤 역할을 하는 도구 모음
# math: 수학과 관련된 도구 모음
# datetime: 날짜와 시간을 다루는 도구 모음
# os: 파일 또는 운영체제 접근

# from math import *
#1단계
import math
math.pi  #하면 math 기능 다 불러옴
# 모듈이용시 math를 일일히 붙이기 싫으니까
# 2단계
from math import *
sqrt(100)
pi

import datetime
now = datetime.datetime.now()  # datetime이라는 클래스
print(now)

#간략하게
from datetime import *
now = datetime.now()

import os
p = os.path.join(os.environ['USERPROFILE'],'DESKTOP')
folder_name = "메가스터디 커피킹"
new_p = os.path.join(p,folder_name)
os.makedirs(new_p)
# 스스로 폴더를 만들어줌, 자동화 할때



