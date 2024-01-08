# string _advance
coffee = "americano" #str
# 내장함수 [int(),str(),float()]
# len(): 문자열의 길이를 반환합니다.
#str.upper() : 문자열의 모든문자를 대문자로 변환
#string.lower() : 문자열의 모든문자를 소문자로 변환
# str.capitalize() : 문자열의 첫문자를 대문자로, 나머지는 소문자로 변환
# str.count(item): 문자열의 item의 개수를 변환합니다. 찾지 못하면 -1을 반환
# str.strip() : 문자열의 앞과 뒤에서 공백과 개행문자를 제거 합니다.
# str.find(sub): 부분 문자열 sub이 시작되는 첫번째 인덱스를 반환합니다. 찾지못하면 -1을 반환합니다.
#string.isupper() : 모든 문자가 대문자인지 확인 값: boolean으로 나옴
#string.islower() : 모든 문자가 소문자인지 확인 값: boolean으로 나옴



# 문제1 대소문자 변환 프로그램
#사용자로 부터 소문자로 된 문자열을 입력받은후 이를 모두 대문자로 변환하는 프로그램

word = (input("소문자 입력:"))
print(word.upper())


#노래 가사에서 단어 카운트
#charlie puth 의 노래 left and right에서 left와 right라는 단어가 각각 몇번나오는지 세는 프로그램 대소문자없이

#song ="""
Memories follow me left and right
I can feel you over here, I can feel you over here
You take up every corner of my mind (what you gon' do now?)
Ever since the d-day y-you went away (no, I don't know how)
How to erase your body from out my brain (what you gon' do now?)
Maybe I should just focus on me instead (but all I think about)
Are the nights we were tangled up in your bed
Oh no (oh no)
Oh no (oh no)
You're goin' 'round in circles
Got you stuck up in my head, yeah
Memories follow me left and right
I can feel you over here, I can feel you over here
You take up every corner of my mind
Your love stays with me day and night
I can feel you over here, I can feel you over here
You take up every corner of my mind (what you gon' do now?)
Ever since the d-day y-you went away (someone tell me how)
How much more do I gotta drink for the pain (what you gon' do now?)
You did things to me that I just can't forget (now all I think about)
Are the nights we were tangled up in your bed
Oh no (oh no)
Oh no (oh no)
You're going 'round in circles
Got you stuck up in my head, yeah
Memories follow me left and right
I can feel you over here, I can feel you over here
You take up every corner of my mind (of my mind)
Your love stays with me day and night
I can feel you over here, I can feel you over here
You take up every corner of my mind (what you gon' do now?)
Did you know you're the one that got away?
And even now, baby, I'm still not okay
Did you know that my dreams, they're all the same
Every time I close my eyes?
Memories follow me left and right
I can feel you over here, I can feel you over here
You take up every corner of my mind (what you gon' do now?)
Your love stays with me day and night
I can feel you over here, I can feel you over here
You take up every corner of my mind (what you gon' do now?)
(Whoa)
I can feel you over here, I can feel you over here
You take up every corner of my mind (what you gon' do now?)

"""

print(f"가사에서 left는 {song.count('left')}개, right는 {song.count('right')}개")
print(f"가사의 길이는 {len(song)}")