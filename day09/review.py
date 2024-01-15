#1~100 사이 정수 유저 입력 n
num = int(input("1~100 정수입력"))

for i in range(101):
    if i % num == 0: # 배수공식
     print(i)


n = int(input("1~100 정수입력"))
for i in range (1,10): # 1~9
    print(f"{n} * {i} = {n * i}")


