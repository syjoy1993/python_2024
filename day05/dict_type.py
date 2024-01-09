# # dict_type
#
# # key - value 짝꿍
# # key 의 특징: 중복 안됨, 숫자 or 문자 type만 가능!
# # value 의 특징: 중복 가능, any type
# zodiac = { # # dict_type 의 시작
#     #키값:value값
#     1:'쥐',
#     2:'소',
#     3:'호랑이',
#     4:'토끼',
#     5:'용'
# }
# print(zodiac[1])
#
# # print(zodiac[키값]) => 키값에 해당하는 value값이 출력된다.

mbti = {
    'e':'외향적',
    'i':'내향적',
    's':'감각적',
    'n':'직관적',
    'f':'감성적',
    't':'이성적',
    'j':'계획적',
    'p':'즉흥적'
}
#print(mbti['e'])   #ctrl + space누르면 자동으로 나옴

# quiz 유저에게 mbti를 입력받고 entj라면 당신은 외향적이고 직관적이고 이성적이고 계획적이시네요 나오게 만들어 주세요

# 내가한거
# personality = input("mbti를 입력하세요")
# print(f"당신은 {mbti[personality]}이고 {mbti[personality]}이고, {mbti[personality]}이고,{mbti[personality]}이시네요")
# personality = input("mbti를 입력하세요")

personality = input("mbti를 입력하세요")  #entj
print(personality[0]) # e 문자열의 첫번째 선택하고 출력
print(f"당신의 성향은  {mbti[personality[0]]} {mbti[personality[1]]} {mbti[personality[2]]} {mbti[personality[3]]}")