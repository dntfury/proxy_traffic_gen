#dntfury
                            
      
import requests
from itertools import cycle
import traceback
#PASTE PROXY HERE
proxies = [
'0.0.0.0:8080',
'ip:port',
'ip:port'

]
#proxies = get_proxies()
proxy_pool = cycle(proxies)
 
url = 'http://www.example.com/'

for i in range(1,50):
    #Get a proxy from the pool
    proxy = next(proxy_pool)
    print("Request #%d"%i)
    try:
        response = requests.get(url,proxies={"http": proxy, "https": proxy})
        print("REQUESTED VIA:",proxy)
        print(response)
    except:
        #When proxy will get connection errors. 
        # just leave that  
        print("skipping.  error")
