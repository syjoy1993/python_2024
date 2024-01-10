#set_data
# datatype
# int, float, str, list, dict



megastudy = {
    'python': [1, 2, 3],
    'java': [1, 3, 5],
    'c': [2, 4, 6]
}


# python 날짜 가져오기
megastudy['python']  # 연산자
megastudy.get('python') # 기능
print(megastudy.get('jva','수업 없음')) # 뒤에꺼로 대체  // 수업 없음
print(megastudy.keys())  # dict_keys(['python', 'java', 'c'])
# 데이터 타입은,,, 아직 모름 그래서 리스트 화 해줘야한다!

print(list(megastudy.keys())) # 키값만 전부  ['python', 'java', 'c']
print((megastudy.values()))
print(list(megastudy.values()))  # 밸류값만 전부  [[1, 2, 3], [1, 3, 5], [2, 4, 6]]
print(list(megastudy.items())) # 전부 다 출력  [('python', [1, 2, 3]), ('java', [1, 3, 5]), ('c', [2, 4, 6])]



#
# my_dict = {
#     'name': 'Alice',
#     'age': 25
#
# }
#
# print(my_dict['name'])  # Alice
# print(my_dict.get('name'))
# print(my_dict.get('gender', 'not Sepcified')) #  (기본값사용)
#
# my_dict = {
#     'name':'bob',
#     'age': 30,
#     'job':'developer'
# }

# #keys
# print(list(my_dict.keys()))
#
# #values
#
# print(list(my_dict.values()))
#
# #items
# print(list(my_dict.items()))