import urllib.request
from bs4 import BeautifulSoup

prefix = "https://www.ceneo.pl/"
postfix = "/opinie-"
product_id = "45498942"
page_num = 1

url = prefix + product_id + postfix + str(page_num)

#pobranie zawartości strony
site = urllib.request.urlopen(url)
page = site.read()

#parsowanie kodu strony
page_tree = BeautifulSoup(page, 'html.parser')


opinions_num = int(page_tree.find("span", attrs={"itemprop": "reviewCount"}).string)
print(opinions_num)


#zapisanie danych do bazy



#pojedyncza opinia: li.review-box
#autor: div.reviewer-name-line
#rekomendacja: div.product-review-summary > em
#gwiazdki: span.review-score-count
#data wystwaienia opinii: time (wartość atrybutu datetime) - pierwsze wystąpienie
#data zakupu produktu: time (wartość atrybutu datetime) - drugie wystąpienie
#treść: p.product-review-body
#wady: div.cons-cell > ul > li
#zalety: div.pros-cell > ul > li
#przydana: [id^=votes-yes]
#nieprzydatna: [id^=votes-no]
#id opinii: li.review-box (wartość atrybutu data-entry-id)
#liczba opinii: span[itemprop=reviewCount]