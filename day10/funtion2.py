
# 매개변수 리스트 2개를 받고 그거를 딕셔너리화 해서 돌려주는 함수를 만들어보기

#해보기
def makeListDictMe(xList,yList,xkey,ykey):
    return {i:{xkey: ykey} for i,(xkey,ykey) in enumerate(zip(xList,yList))}

breads1 = ['소금빵', '보름달', '단팥빵', '앙버터', '마카롱']
prices1 = [2500, 1000, 2400, 4500, 3000]
b = makeListDictMe(breads1,prices1,'빵','가격')
# print(b)



# 수업
def makeListDict(xList,yList,xkey,ykey):
    return [{xkey:x,ykey:y}for x,y in zip(xList,yList)]

breads = ['소금빵', '보름달', '단팥빵', '앙버터', '마카롱']
prices = [2500, 1000, 2400, 4500, 3000]


a = makeListDict(breads, prices ,'빵','가격')
# print(a)


# xkey값은 item, ykey은 price default 설정하기
def makeListDict(xList,yList,xkey = 'item',ykey = 'price'):
    return [{xkey:x,ykey:y}for x,y in zip(xList,yList)]
c = makeListDict(breads,prices)
print(c)


