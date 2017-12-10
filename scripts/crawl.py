from bitlycrawler import CrawlerVerAPI, CrawlerVerMaint
import string
from itertools import product
import apikey
import requests
import sys
import traceback
import time

def main():
    bitly_apikey = apikey.bitly_apikey["vernal"]
    base_target_url = "https://bitly.com/"
    target_url = "http://73spica.tech/blog/"
    target_url = "https://bit.ly/2AaaPsX"
    target_url = "https://bitly.com/b4yqKg"
    target_url = "https://bitly.com/a"

    f = open("output/one-test.txt","w")

    for i in range(3000):
        bf = True
        while bf:
            try:
                target_url = base_target_url + "gz"
                info = CrawlerVerMaint.get_link_info(target_url)
                if info:
                    f.write(info+"\n")
                    bf = False
                else:
                    f.write("It's NoneType.\n")
                    time.sleep(5)
            except:
                f.write("Error.\n")
                time.sleep(5)
        break
        time.sleep(5)
    return

    #f = open("short-long.txt","w")
    f = open("test3.txt","w")
    chrs = string.ascii_letters + string.digits
    for i,x in enumerate(product(chrs, repeat=2)):
    #for x in product(chrs, repeat=2):
        short_hash = "".join(x)
        #print(short_hash)
        target_url = base_target_url + short_hash
        try:
            info = CrawlerVerMaint.get_link_info(target_url, 10)
            if info:
                f.write(info+"\n")
            continue
            if info:
                out = "%s | %s\n"%(short_hash,info["base_info"]["long_url"])
            else:
                out = "%s | %s\n"%(short_hash, "Not exist.")
            f.write(out)
        except requests.exceptions.ConnectionError as err:
            print("ConnectionError:", err)
            print("Now: %d : %s"%(i, short_hash))
        except Exception as e:
            print("Unexpected error:", sys.exc_info()[0])
            traceback.print_exc()
            print("Now: %d : %s"%(i, short_hash))
    f.close()
    return
    print( CrawlerVerAPI.get_link_info(bitly_api_key, target_url) )

if __name__ == "__main__":
    main()
