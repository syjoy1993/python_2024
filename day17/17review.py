words = ['apple', 'banana', 'cherry', 'date']
def solution(x):
   lenth = [len(i) for i in x]
   lenth_count = [lenth.count(i) for i in lenth]
   return {x:y for x,y in zip(lenth,lenth_count)}

a = solution(words)
print(a)
# 위에 코드 가능!!!!!!!!!!!!!!

# # 답
# def solution(arr):
#    result = {}
#    for i in arr:
#       length = len(i)
#       if length in result: # 길이가 있으면
#          result[length] += 1 # 값을 1씩올려줘
#       else:
#          return [length] = 1
#       return result
#    #결과 {5: 1, 6: 2, 4: 1}
#
# ㅋㅋ
