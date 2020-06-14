import requests
from urllib.parse import quote

def all_product():
        #homepage url
        JGP_home = "https://www.609.com.tw/Country"
        home_page = requests.get(JGP_home).text
        home_page = home_page.split("\n")

        for line in home_page:
            if "var allMain" in line:
                start = line.index("[")
                end = line.index("]")
                product_list = line[start+2:end-1].replace("\"", "")
                break
        product_list = product_list.split("},{")
        product_dic = {}

        for item in product_list:
                item = item.split(",")
                name = item[2][6:]
                category = item[0][7:]
                try:
                        product_dic[category].append(name)
                except:
                        product_dic[category] = [name]
        return product_dic

def get_JPG_price(name):
        price_url = "https://www.609.com.tw/Parts/PartQuery/" + name
        price_page = requests.get(price_url).text
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

