# dict_comprehension

coffee = ['아메리카노', '라떼','바닐라']
price = [2500, 3000, 3500]
caffeine = [120, 150, 50]

# # dict 순차적으로
# 기본형 :[  for i in range()}
# zip화 : [for x,y in zip(coffee,price)] x는 커피의 미지수 y는 프라이스의 미지수를 집으로 묶음
# enumerate화 : [for x,y in enumerate(zip(coffee,price))] x는 커피의 미지수 y는 프라이스의 미지수를 집으로 묶은걸 순서를 매김
# enumerate화를 해서 변수에 담아줌 : [for index,(x,y) in enumerate(zip(coffee,price))]
# x는 커피의 미지수 y는 프라이스의 미지수를 집으로 묶은걸 순서를 매긴걸 미지수에 넣어줌
#
# dict_형태로 출력할꺼니까 {for index,(x,y) in enumerate(zip(coffee,price))} 딕에 담아줌
#
# dict으로 들어갈때 변수들이 어떤 관계로 들어갈지 적어줌  {index:{'name':x,'price':y}for index,(x,y) in enumerate(zip(coffee,price))}


# 몇번쨰인지 알고싶어요~!
#enumerate화 (열거라는뜻)시켜준다!!!!!!!!!!!

fruits = ['apple', 'mango', 'banana']

for index,i in enumerate(fruits): # index와 i는 미지수
    print(f"{index}.{i}")
# 0.apple
# 1.mango
# 2.banana
coffee = ['아아','라떼','콜드블루']
price = [5000,6000,5000]
#for c,p in zip(coffee,price):  # 2개의 값 두개 변수 필요 여기서 c,p// 남남인 리스트 묶어줌
coffeeDict = {i:{'이름':c,'가격':p}for i,(c,p) in enumerate(zip(coffee,price))}
#딕트 모양새는 처음 키는 index가 들어갈꺼고 그 키의 밸류도 딕트 인데 거기는 키값은 이름이고, 그 키의 밸류는 c가 될꺼고, 두번째 키는 가격이고 그밸류는 p가 될꺼야

print(coffeeDict) # {0: {'이름': '아아', '가격': 5000}, 1: {'이름': '라떼', '가격': 6000}, 2: {'이름': '콜드블루', '가격': 5000}}
