#set_data (집합) 중복안됌
# dict랑 비슷하게 {}, but 키가 없음

a = {1, 2, 3, 1, 2, 3, 1, 2, 3} # 직접적 set  //{1, 2, 3}
print(a)

# set화가 가능
b = set([1, 2, 3, 4, 1, 2, 3]) #[1, 2, 3,4,1,2,3]리스트
print(b)
# 셋트화 하면 {1, 2, 3, 4}


article = """
By Marita Moloney & Patrick Jackson
BBC News
Ecuador's president has ordered that criminal gangs be "neutralised" after days of violence culminated in an attack on a television studio.

Masked gunmen broke into public television channel TC's live studio during a broadcast, forcing staff to the floor.

Police made 13 arrests following the attack, which injured two employees.

At least 10 people have been killed since a 60-day state of emergency began in Ecuador on Monday.

The emergency was declared after a notorious gangster vanished from his prison cell. It is unclear whether the incident at the TV studio in Guayaquil was related to the disappearance from a prison in the same city of the boss of the Choneros gang, Adolfo Macías Villamar, or Fito as he is better known.

"""

wordList = article.split(' ')

wordList.sort()  #정렬 중복된  리스트로 됨 sort는 한번에 프린트가 안되나봄
c = list(set(wordList)) # 셋트화 해서 리스트의 기능이 없어짐, 그래서 중복과 정렬이 안된 상태에서 리스트화
c.sort()  #그래서 중복과 정렬이 안된 상태에서 리스트화 한걸 다시 sort해서 정렬함
print(c) # 중복 안되고 정렬된 리스트로 출력됨

#
# wordList.sort()  #정렬 중복된 리스트임 리스트로 됨 sort는 한번에 프린트가 안되나봄
# print(wordList)
#
# print(set(wordList)) #중복되지 않은 00이 됨 set 화, sort된게 없어짐, 그래서 랜덤 상태
#
# print(list(set(wordList)))  #중복되지 않은 리스트가 됨


# set(집합) 중복안됨

a = {1, 2, 3, 1, 2, 3, 1, 2, 3}
b = set([1, 2, 3, 4, 1, 2, 3])

b.add(8) # 추가 1은 추가 해도 안됨 중복안됨으로
b.update([5,6])

# b.add(5) # 추가 하면 뒤에 5가 생김
# b.discard(3) # 3빠짐 있는 것중에 3빠짐
# print(b)
# b.clear() # 전부 없앰 셋트 타입이에요 만 알려줌 set()
print(b)