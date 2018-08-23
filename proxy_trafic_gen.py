print("*************************BY DNT FURY***************************")
#by developerfury@gmail.com                             
      
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
        #When proxy will get connection errors. We will have to try the entire request using another proxy to work. 
        #We will just skip that one 
        print("Skipping. Connnection error")
