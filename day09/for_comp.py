# #for_comp-기본
# for 중요함, 심화 버전임

a = []
for i in range():
    a.append(i)
# 위에 축약

a = [i for i in range(1001)]

b = [i for i in range(101)] # 1?0?~100
c = [i for i in range(1,501)]# 1~500
d = [i for i in "megastudy"]
#[i for i in range(1,101)] # 1~100
e = [i*2 for i in range(1,101)] # 2~200

# 1. 1~10을 각각 제곱한 수의 리스트
f = [i**2 for i in range(1,11)]

#2. 1~10에 각가 5를더한 리스트
g = [i+5 for in i range(1,11)]