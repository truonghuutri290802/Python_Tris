
from newspaper import Article
url = 'https://vnexpress.net/12-000-nguoi-do-ve-cua-lo-4092705.html'
article = Article(url)
article.download()
article.parse()
# Xong rồi đấy, giờ lấy data thôi
print(article.title)
