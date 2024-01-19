#reduce_test

#map 치환
#filter필터링
#reduce 누적
#reduce 내장이 아니여서~ from functools import reduce 불러와야됨

from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x,y: x+y,numbers)
print(result)

mult_result = reduce(lambda x,y: x*y,numbers)
print(mult_result)