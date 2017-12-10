"""
短縮URLクローリングモジュール
"""

import requests
from bs4 import BeautifulSoup
import re
import json
from itertools import product
import string
from time import sleep

# Bitly My Page
#  - https://app.bitly.com/Bhbr4V3UGjq/bitlinks/2AaaPsX
# In Bitly, We can access an analytics page by adding "+" the target shortener URL.
#    - http://bit.ly/2AaaPsX
#    -> http://bit.ly/2AaaPsX+

# In Bitly, the method for crawling is three.
# i) Analytics Page Access
# ii) Using API
# iii) Auto brawsing

class CrawlerVerMaint:
    """tinyurlのクローリングのためのクラス"""

    BASE_MAINT_URL = "https://preview.tinyurl.com/"
    
    def __init__(self):
        pass

    @staticmethod
    def get_page(target_url):
        """引数のURLへGetした結果を返す関数"""
        r = requests.get(target_url)
        return r.text

    @staticmethod
    def get_link_info(short_url, redo=5):
        """短縮URLの情報を取得し整形して返す関数"""
        pass
        

def main():
    bitly_api_key = "c7e7f54b82da0a00900f776d5e1c2bf6308b2427"
    base_target_url = "https://bitly.com/"
    target_url = "http://73spica.tech/blog/"
    target_url = "https://bit.ly/2AaaPsX"
    target_url = "https://bitly.com/b4yqKg"
    target_url = "https://bitly.com/a"
    ex_url = "https://tinyurl.com/6rmuv"
    short_hash = "6rmuv"
    ex_maint_url = "https://preview.tinyurl.com/6rmuv"
    help(CrawlerVerMaint)
    return

    print(CrawlerVerMaint.get_page(ex_maint_url))

    return

    f = open("short-long.txt","w")
    chrs = string.ascii_letters + string.digits

if __name__ == "__main__":
    main()
