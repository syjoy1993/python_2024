#function_part2


# 가변매개변수

def makePizza(*toppings):
    print("다음 피자는 아래의 토핑이 들어갑니다.")
    for i in toppings:
        print(i)

makePizza("pineapple")
makePizza("pineapple","cheese")
makePizza("pineapple","cheese","mushroom")

# 퀴즈
# [리스트 형태로 '닭, '돼지, '소'] = zodiac(년도 입력)
# 내가한거,,,,,,,,,,,,,,
# def zodiac(*bornYears):
#     print("태어난 년도를 적으면 해당 띠가 나옵니다.")
# ['닭' if i == o '돼지' elif i == 1 else '소' for i in bornYears]


def zodiac(*years):
    print("태어난 년도를 적으면 해당 띠가 나옵니다.")
    sign = ['닭띠','개띠','돼지띠','쥐띠','소띠','호랑이띠','토끼띠']
    newList = []
    for i in years:
        newList.append(sign-[i-1993])
    return newList

a = zodiac(1993,1994,1999,2002)
print(a)

def zodiac(*years):
    sign = ['닭띠','개띠','돼지띠','쥐띠','소띠','호랑이띠','토끼띠']
    return [sign[i - 1993] for i in years]

a = zodiac(1993,1994,1999,2002)
print(a)




