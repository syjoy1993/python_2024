#join
#word = '_'.join(['ice','cream']) #'ice  creea'

id = input("아이디 입력:")
domain = input("도메인 입력:")
#'@'.join
print('@'.join([id,domain]))

article = """
US Congress leaders have reached a deal over the total amount of spending for the rest of 2024 as they seek to avoid a partial government shutdown, local media report.

The $1.6tn (£1.2tn) figure includes $886bn for defence and more than $704bn for non-defence spending, according to Republican House Speaker Mike Johnson.

However, there appears to be some discrepancy over the numbers.

The deal now needs approval from the House of Representatives and Senate.

They have less than two weeks to finalise funding and stop the suspension of some federal services.

"""
newArticle = article.replace('after','before')
newArticle1= newArticle.replace('it','😄😄')
print(newArticle1)
newArticle = article.replace('after','before').replace('it','😄😄')

newArticle = article.replace('after','before').replace('it','😄😄').split()

