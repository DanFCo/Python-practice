import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/john-lewis-partners-abraham-office-chair/tan/p3361768")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class": "price price--large"})
string_price = element.text.strip()

price_without_symbol = string_price[1:]

price = float(price_without_symbol)

# print(price) will print the price!

# if price < 500:
#     print("buy the chair")
#     print("the current price is {}".format(price))
# else:
#     print("over budget, do not buy")

# print(float(price_without_symbol)< 400) will print true!


#print(element) will give you the whole element.. but we only want the text within the html
#print(element.text) will give us just the text inside the element
# <p class="price price--large"> £299.00 </p>
