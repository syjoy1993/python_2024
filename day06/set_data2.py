#set_data (집합) 중복안됌

a = {1, 2, 3, 1, 2, 3, 1, 2, 3}
b = set([1, 2, 3,4,1,2,3])
b.add(1)
b.add(5)
b.discard(3)
print(b)
b.clear()
print(b)