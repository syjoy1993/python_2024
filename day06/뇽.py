
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

wordList.sort()  #정렬 중복된 리스트임 리스트로 됨 sort는 한번에 프린트가 안되나봄
print(wordList)

print(set(wordList)) #중복되지 않은 00이 됨 set 화, sort된게 없어짐, 그래서 랜덤 상태

print(list(set(wordList)))  #중복되지 않은 리스트가 됨