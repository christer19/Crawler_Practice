import requests
from urllib.parse import quote

def get_JPG_price(name):
        MY9_url = "http://www.my9.com.tw/adv-search/result.php?keyword=" + name + "&submit=%E6%90%9C%E5%B0%8B"
        price_page = requests.get(MY9_url).text
        name = []
        price = []
        name_frame = price_page.split("h6")
        for i in range(len(name_frame)):
                if i % 2 == 1:
                        name.append(name_frame[i].split(">")[1].strip("</"))
        
        price_frame = price_page.split("NT$")
        for j in range(len(price_frame)):
                if j % 2 == 1:
                        price_temp = str()
                        for k in price_frame[j]:
                                if k == "/":
                                        break
                                price_temp += k
                        price.append(price_temp)

        return name, price

