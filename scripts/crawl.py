from bitlycrawler import CrawlerVerAPI, CrawlerVerMaint
import string
from itertools import product
import apikey

def main():
    bitly_apikey = apikey.bitly_apikey
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
