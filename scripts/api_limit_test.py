from bitlycrawler import CrawlerVerAPI, CrawlerVerMaint
import string
from itertools import product
import apikey
import requests
import sys
import traceback
import time


def main():
    bitly_apikeys = apikey.bitly_apikey
    chrs = string.ascii_letters + string.digits

    # とりあえず適当な一つのAPIキーの利用制限を見る
    # 3000くらいならいけそうだから3文字くらいでやってみようかな
    for x in product(chrs,repeat=3):
        short_hash = "".join(x)
        print(short_hash)
        break
        print(CrawlerVerAPI.get_link_info(bitly_apikeys["vernal"], "aa"))
    

if __name__ == "__main__":
    main()
