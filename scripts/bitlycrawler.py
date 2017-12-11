import requests
from bs4 import BeautifulSoup
import re
import json
from itertools import product
import string
from time import sleep

"""
Bitly My Page
 - https://app.bitly.com/Bhbr4V3UGjq/bitlinks/2AaaPsX
In Bitly, We can access an analytics page by adding "+" the target shortener URL.
   - http://bit.ly/2AaaPsX
   -> http://bit.ly/2AaaPsX+

In Bitly, the method for crawling is three.
i) Analytics Page Access
ii) Using API
iii) Auto brawsing
"""

class CrawlerVerAPI:
    """bit.lyのクローリングのためのクラス"""

    BASE_API_DOMAIN = "https://api-ssl.bitly.com"
    BASE_BITLY_DOMAIN = "https://bit.ly/"
    BASE_JMP_DOMAIN = "http://j.mp/"
    """
        BASE_API_DOMAIN  : APIのためのURL
        BASE_BITLY_DOMAIN: bit.lyの短縮URLのドメイン
        BASE_JMP_DOMAIN  : j.mpの短縮URLのドメイン 
    """

    def __init__(self):
        pass

    @classmethod
    def do_shortener(cls, api_key, long_url):
        """
            APIキーとLongURLを渡すと短縮URLを生成しそのURLを返す
        """
        shortener_path = "/v3/shorten"
        shortener_query = "?access_token={}&longUrl={}".format(api_key, long_url)
        api_url = cls.BASE_API_DOMAIN + shortener_path + shortener_query
        r = requests.get(api_url, timeout=2)
        return r.text

    @classmethod
    def get_link_info(cls, api_key, short_url, target="b"):
        """
            APIキーと短縮URLを指定するとそのリンク先の情報を返す
        """
        target_domain = ""
        if target == "b":
            target_domain = cls.BASE_BITLY_DOMAIN
        elif target == "j":
            target_domain = cls.BASE_JMP_DOMAIN
        else:
            print("Invalid target.")
            return
        shortener_path = "/v3/link/info"
        if not short_url.startswith(target_domain):
            short_url = target_domain + short_url
        shortener_query = "?access_token={}&link={}".format(api_key, short_url)
        api_url = cls.BASE_API_DOMAIN + shortener_path + shortener_query
        r = requests.get(api_url, timeout=2)
        return r.text

    @classmethod
    def api_limit_test(cls, api_key, short_url):
        pass

class CrawlerVerMaint:
    BASE_API_URL = "https://api-ssl.bitly.com"
    
    def __init__(self):
        pass

    @staticmethod
    def get_link_info(short_url, redo=5):
        url = short_url + "+"
        # redo回までに目的のデータが取れればreturnで帰る
        for i in range(redo):
            try:
                r = requests.get(url, timeout=1)
                soup = BeautifulSoup(r.text, 'lxml')
                r = re.compile("{.+}")
                for tag in soup.find_all("script", attrs={"type": "text/javascript"}):
                    jscode = tag.text
                    if "long_url_no" in jscode:
                    #if jscode != "": # これだとgetTimeとかいうのが入った時に取れない
                        # 今回は数も少ないしどうせリストにするのでfindall使おうかしら
                        #for m in r.finditer(jscode):
                        #    print(m.group())
                        return jscode
                        results = r.findall(jscode) # TODO: この条件で取れてない可能性
                        ret = {}
                        ret["base_info"] = json.loads(results[0])
                        ret["click"] = json.loads(results[1])
                        ret["user_info"] = json.loads(results[2])
                        ret["others"] = json.loads(results[3])
                        return ret
            except requests.exceptions.ConnectionError as err:
                print("ConnectionError:", err)
                raise err
            except Exception as e:
                print("Unexpected error:", sys.exc_info()[0])
                raise e
            #sleep(1)
        # ここに来てたら，該当のJSコードがなかったということ
        return None

