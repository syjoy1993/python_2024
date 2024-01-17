
movieList = ['액션영화', '로코', '다큐']
price1 = [12000,10000,11000]
snackPack = ['팝콘세트', '스낵콤보','건강 팩']
price2 = [6000,8000,7000]
upGrade= ['일반좌석', '프리미엄', 'vip']
price3 = [0,5000,10000]

# discount age< 18: 20%할인, age <= 65 ,15%할인
#
# 나이, 종류,스낵팩,좌석 업글

def priceDic (xList,ylist,i=0,x='item',y='price'):
    return {i+1:{'item':x,'price':y} for i,(x,y) in enumerate(zip(xList,ylist))}
a = priceDic(movieList,price1,0,'movieitem','price')
b = priceDic(snackPack,price2,0,'snackPack','price2')
c = priceDic(upGrade,price3,0,'seat','price3')
print(a)
print(b)
print(c)
# #여기까지


cgv = {
    1: a,
    2: b,
    3: c
}

# cgv 딕셔너리를 만들었음, 이제 제시문 보여주고 입력받기

userlist = []
for i in range(3):
    if i == 0:
        userlist.append(int(input(f"영화 1.액션영화 2.로맨틱 코메디 3.다큐멘터리  를 골라주세여")))
    elif i == 1:
        userlist.append(int(input(f"snack pack 1.팝콘세트 2.스낵콤보 3.건강팩")))
    else:
        userlist.append(int(input(f"좌석을 업그레이드 할까요? 1.일반좌석 2.프리미엄 3.VIP")))


#선택헤서 계산하기
print(f"선택한 영화{cgv[1][userlist[0]]['item']}, 선택한 snack pack{cgv[2][userlist[1]]['item']}, 선택한 좌석{cgv[3][userlist[2]]['item']} 입니다")

totalprice = (cgv[1][userlist[0]]['price'] + cgv[2][userlist[1]]['price'] + cgv[3][userlist[2]]['price'])
userAge = int(input(f"나이를 선택하세요 1. 12세 미만 2. 65세이상 3. 13세~64세"))

if userAge == 1:
    totalprice * 0.8
    print(f" 총금액은{totalprice * 0.8}입니다")

elif userAge == 2:
    totalprice * 0.85
    print(f" 총금액은{totalprice * 0.85}")

else:
    totalprice
    print(f" 총금액은{totalprice}")
