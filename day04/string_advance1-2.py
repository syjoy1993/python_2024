a = "mega"
b = "study"
c = a + b #문자열 연결 연산자 // megastudy
e = a * 3  # 문자열 반복   /studystudystudy
d = a[0] # [] 문자열 인덱싱 결과 :m
f = b[0:3] #[syart :end] 문자열 슬라이싱 end 제외 결과: stu
g = 'g' in a # "mega" 에서 'g'가 있니? 결과: True or False

# split
title = "megastudy python programming"
print(title.split()) # 빈공간 기준으로 str에서 list들어 주기
title1 = "orange,apple,banana"
print(title.split(','))


#유저한테 이메일 주소르 받고 -> ['유저아이디', '도메인']
#Ex) python@megastudy.com []

#print(user.split('@'))
#list[1].split('.')
user = input("이메일 주소 입력") #['python','megastudy.com']
a = user.split("@") #['python','megastudy.com']
b = a[.].split('.') #['megastudy', 'com']
a[1] = b[0]
a.append(b[1])  #a[2] = b[1]가 a[2]없으므로 안됨
print(a)