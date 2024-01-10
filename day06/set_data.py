#set_data
# datatype
# int, float, str, list,dict

my_dict = {
    'name': 'Alice',
    'age': 25

}
print(my_dict['name']) # Alice
print(my_dict.get('name'))
print(my_dict.get('gender', 'not Sepcified')) #  (기본값사용)

my_dict = {
    'name':'bob',
    'age': 30,
    'job':'developer'
}

#keys
print(list(my_dict.key()))

#values

print(list(my_dict.values()))

#items
print(list(my_dict.items()))