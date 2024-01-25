# Qrcode만들기


import qrcode

url = 'https://www.instagram.com/riize_official/'
img = qrcode.make(url)  # 이미지는 큐알코드로 만든 url 이여
img.save('./riiz.png') # 위에 이미지를 현재 폴더에 (안에 이름으로)저장해조
img.save('바탕화면/riiz.png') # 위에 이미지를 다른파일에 저장 하고 싶으면(안에 이름으로)저장해조
