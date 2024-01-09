# 리스트 기능
# 1. 리스트의 길이 기능 : len()
store = ['cu', 'gs', 'seven','ministop']
print(len(store)) # 4가 출력됨

# 2. 리스트 추가[맨뒤]: append('무엇을')
store.append('emart24')
print(store)
#['cu', 'gs', 'seven', 'ministop', 'emart24']

# 3. 리스트 추가 [몇번째]: insert(몇번째,'무엇을')
store.insert(2, 'familymart')
print(store)
#['cu', 'gs', 'familymart', 'seven', 'ministop', 'emart24']

# 4. 리스트 제거: remove('무엇을')
store.remove('cu')
print(store)
#['gs', 'familymart', 'seven', 'ministop', 'emart24']

# 5.리스트 해당 아이템 위치 찾기: index('무엇을') -> 인덱스로 출력
print(store.index('ministop'))
# 3

# 6. 리스트에 해당 아이템 몇개 인지 갯수 세기 : count('무엇을') //리스트 안에 몇개인가여?
print(store.count('emart24'))

# 1

# 7.리스트를 추가: extend(리스트) // +[더하기와 같은 역할]
newStore = ['storyway', 'buytheway']
store.extend(newStore)
print(store)

# 결과 ['gs', 'familymart', 'seven', 'ministop', 'emart24', 'storyway', 'buytheway']

# 8. 리스트 정렬: sort() -> 특수기호->숫자->알파벳순으로 정렬됨
store.sort()
print(store)

# 결과 ['buytheway', 'emart24', 'familymart', 'gs', 'ministop', 'seven', 'storyway']
store.sort(reverse=True)
print(store)



