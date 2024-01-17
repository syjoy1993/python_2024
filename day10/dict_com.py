# dict_comprehension
nomalPopcorn = {
    'name':'일반팝콘',
    'price':2500,
}


coffee = ['아메리카노', '라떼','바닐라']
price = [2500, 3000, 3500]
caffeine = [120, 150, 50]
#zip!
# #zipper 두개의 요소를 묶어줌 (a, b)로
# ziped = zip(coffee,price)
# print(list(ziped))  #[('아메리카노', 2500), ('라떼', 3000), ('바닐라', 3500)]


#  comprehension 사용

result = [{'이름':x, '가격':y}for x,y in zip(coffee,price)]
print(result)  # [{'이름': '아메리카노', '가격': 2500}, {'이름': '라떼', '가격': 3000}, {'이름': '바닐라', '가격': 3500}]


#나
caffeineResult = [{'이름':x, '가격':y, '카페인':z} for x,y,z in  zip(coffee,price,caffeine)]
print(caffeineResult)  #[{'이름': '아메리카노', '가격': 2500, '카페인': 120}, {'이름': '라떼', '가격': 3000, '카페인': 150}, {'이름': '바닐라', '가격': 3500, '카페인': 50}]


# 최종 보스

#for i in coffee:  # i= 아메리카노, 라떼, 바닐라  만약 i가 몇번쨰 인가요? 알고싶다면
for index,item in enumerate(coffee):   # 순서와 해당아이템을 나타냄,,,, 미지수 ij 해도 되고 index, item 해도됌
    print(f"{index}. {item}")

    #for문을 쓰면서 리스트, 문자열에서 몇번쨰인지 알고싶다!
    #enumerate를 기억하면 된다.

###

a = {index:{'이름':coffee, '가격':price} for index,(coffee,price) in enumerate(zip(coffee,price))} #enumerate화 하면 몇번째인가? 가 나온다 인덱스가 나옴}
 #index, coffee 와 price는 미지수이다.
 # ==  위 식이 아래 dict을 만든거임
Popcorn = {
    1:{
        'name':'일반팝콘',
        'price':2500
    }
}
# 위 형식을 봤을 떄 index가 값: 1 역할 / (coffee,price) 가 'name':'일반팝콘' 'price':2500 역할

print(a)  #{0: {'이름': '아메리카노', '가격': 2500}, 1: {'이름': '라떼', '가격': 3000}, 2: {'이름': '바닐라', '가격': 3500}}

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
#enumerate화 시켜준다!!!!!!!!!!!
