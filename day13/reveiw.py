my_string =["jaron","bread"]
# "jaron" => "noraj"
# def reversMy(x):
#     strList = [i for i in x]
#
#     return strList
# a = reversMy(my_string)
# print(a)

#ekq
def reversStr(my_string):
    strList = list(my_string)
    strList.reverse()
    word = ""
    for i in strList:
        word += i
    return word

toso_list = ["problemsolving", "practiceguitar", "swim","studygraph "]
finishedList = [True, False, True, False]

#답
def haveto_List(todoList,finishedList):
    newList = [todoList[index]for index,item in enumerate(toso_list,finishedList) if not item]




