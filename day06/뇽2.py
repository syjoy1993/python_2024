news = """
By David Gritten
BBC News
UK and US naval forces have repelled the largest attack yet by Yemen's Houthi rebels on Red Sea shipping,
UK Defence Secretary Grant Shapps says.

Carrier-based jets and warships shot down 21 drones and missiles launched by the Iran-backed group overnight.

The Houthis said they targeted a US ship in retaliation for the killing of rebels who tried to attack
 a container ship by using speed boats last month.

Mr Shapps said he had "no doubt" that Iran was heavily behind such attacks.

Asked about possible Western strikes on Houthi targets in Yemen in response,
he said: "Watch this space."
"""

newsWords = list(news) # 리스트가 됨
print(newsWords)
newsWords.sort()
print(list(set(newsWords)))

