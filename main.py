import sys
import numpy as np
import pandas as pd
import requests
from urllib.parse import quote
import JGP

#酒條通 買酒網 酒瓶到 威士忌分享家 洋酒城

print("Welcome~~")

def exit_program():
    sys.exit(0)


def main():    
    # function menu
    print("1. 酒品比價\n2. 各店瀏覽\n3. 當日特價\n4. 當日價格下載\n5. 製作\n6. 結束\n")
    print("選擇服務")
    act = input()
    
    # check enter
    try:
        act = int(act)
    except:
        print("please enter number...")
        print()
        main()

    # response
    if act == 6:
        exit_program()
    if act > 6:
        print("no such service")
        print()
        main()
















"""
JGP_dic = JGP.all_product()
product = quote(input("買什麼酒?\n").encode("utf-8"))

# check if product exists
exist = 0
for key in JGP_dic:
    for i in JGP_dic[key]:
        if product in i:
            exist = 1

if exist == 0:
    print("no such product")



print(JGP.get_JPG_price(product))









input("exit....")
"""

main()