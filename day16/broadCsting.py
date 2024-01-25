#gTTS
# 구글에서 만든 글자를 읽어주는 아이

from gtts import gTTS
text = "차량번호 19마 1234차주님 제발 카운터로 와주세여"
tts = gTTS(text, lang='ko')
tts.save('result.mp3')