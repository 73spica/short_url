import requests
from bs4 import BeautifulSoup
import re
import json
from itertools import product
import string
from tqdm import tqdm
from time import sleep

# Bitly My Page
#  - https://app.bitly.com/Bhbr4V3UGjq/bitlinks/2AaaPsX
# In Bitly, We can access an analytics page by adding "+" the target shortener URL.
#    - http://bit.ly/2AaaPsX
#    -> http://bit.ly/2AaaPsX+

# In Bitly, the method for crawling is two.
# i) Analytics Page Access
# ii) Using API
# iii) Auto brawsing.

class CrawlerVerAPI:
    BASE_API_URL = "https://api-ssl.bitly.com"
    def __init__(self):
        pass

    @classmethod
    def do_shortener(cls, api_key, long_url):
        shortener_path = "/v3/shorten"
        shortener_query = "?access_token={}&longUrl={}".format(api_key, long_url)
        api_url = cls.BASE_API_URL + shortener_path + shortener_query
        r = requests.get(api_url)
        return r.text

    @classmethod
    def get_link_info(cls, api_key, short_url):
        shortener_path = "/v3/link/info"
        shortener_query = "?access_token={}&link={}".format(api_key, short_url)
        api_url = cls.BASE_API_URL + shortener_path + shortener_query
        r = requests.get(api_url)
        return r.text

class CrawlerVerMaint:
    BASE_API_URL = "https://api-ssl.bitly.com"
    
    def __init__(self):
        pass

    @staticmethod
    def get_link_info(short_url):
        url = short_url + "+"
        try:
            r = requests.get(url)
        except requests.exceptions.ConnectionError as err:
            print("ConnectionError:", err)
        except:
            print("Unexpected error:", sys.exc_info()[0])
        soup = BeautifulSoup(r.text, 'lxml')
        r = re.compile("{.+}")
        for tag in soup.find_all("script", attrs={"type": "text/javascript"}):
            jscode = tag.text
            if jscode != "":
                # 今回は数も少ないしどうせリストにするのでfindall使おうかしら
                #for m in r.finditer(jscode):
                #    print(m.group())
                results = r.findall(jscode)
                ret = {}
                ret["base_info"] = json.loads(results[0])
                ret["click"] = json.loads(results[1])
                ret["user_info"] = json.loads(results[2])
                ret["others"] = json.loads(results[3])
                return ret

def main():
    bitly_api_key = "c7e7f54b82da0a00900f776d5e1c2bf6308b2427"
    base_target_url = "https://bitly.com/"
    target_url = "http://73spica.tech/blog/"
    target_url = "https://bit.ly/2AaaPsX"
    target_url = "https://bitly.com/b4yqKg"
    target_url = "https://bitly.com/a"

    f = open("short-long.txt","w")
    chrs = string.ascii_letters + string.digits
    #for i,x in enumerate(product(chrs, repeat=2)):
    for x in product(chrs, repeat=2):
        short_hash = "".join(x)
        print(short_hash)
        target_url = base_target_url + short_hash
        info = CrawlerVerMaint.get_link_info(target_url)
        out = "%s | %s\n"%(short_hash,info["base_info"]["long_url"])
        f.write(out)
        break
    f.close()
    return
    print( CrawlerVerAPI.get_link_info(bitly_api_key, target_url) )

if __name__ == "__main__":
    main()
