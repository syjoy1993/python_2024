# 모듈간의 상호 작용을 보자
## import my_math가져올께 "함수"와 "클래스" 가져올 수 있음


import my_math
result = my_math.add(20,20)
print(result) # 20

#my_math 이게 너무 길다면!
import my_math as mm
# as mm 이라고 my_math를 부를게
result = mm.add(10,10)


# 난, 함수쓸 때 어디 있는 ~ 이거 쓰기 싫다!
from my_math import add
# from my_math 로 부터 add를 가져올게! 라고 먼저 떄리면
result = add(20,20)
#이렇게 간단하게 쓸수 있다

print(result)

# * universal my_math 여기 있는거 전부다 가져올게
# import * :다른 곳에 있는 모듈들 다쓰겠다 라고 말하는 것
# 다른프로그래밍에서도 볼 수 있다.
from my_math import * # * universal
result = add(20,20)
print(result)
