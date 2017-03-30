import requests
import time
 
url = "http://nba.hupu.com/"
 
starttime = time.time()
 
for i in range(100):
    requests.get(url)
     
endtime = time.time()
 
print("time:%f" % (endtime - starttime))