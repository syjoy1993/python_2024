movieList = ['액션영화', '로코', '다큐']
price1 = [12000,10000,11000]
snackPack = ['팝콘세트', '스낵콤보','건강 팩']
price2 = [6000,8000,7000]
upGrade= ['일반좌석', '프리미엄', 'vip']
price3 = [0,5000,10000]
# discount age< 18: 20%할인, age <= 65 ,15%할인
#
# 나이, 종류,스낵팩,좌석 업글


moviePrice = [{'영화종류':m, 'price':p} for m,p in zip(movieList,price1)]
snackPackPrice = [{'snackpack':s,'price':p} for s,p in zip(snackPack,price2)]
upGradePrice = [{'좌석':u,'추가금':p} for u,p in zip(upGrade,price3)]

print(moviePrice)
print(snackPackPrice)
print(upGradePrice)
cgv = {i:{'영화가격':m,'스낵팩':s,'upgrade':u} for i,(m,s,u) in enumerate(zip(moviePrice,snackPackPrice,upGradePrice))}

print(cgv)
if age < 20:


elif age >= 65:

else: