import requests as rq
from bs4 import BeautifulSoup
import time
import pandas as pd
 
title = []
body = []
publish_time = []
 
 
for page in range(1, 1):
    print("start collecting ctee page {page}".format(page=page))
    home_url = "https://ctee.com.tw/livenews/aj/page/" + str(page)
    r = rq.get(home_url)
    soup = BeautifulSoup(r.text, "lxml")
 
    for i in range(0, len(soup.select("div.item-content"))):
        url = soup.select("div.item-content")[i].select("a")[1]["href"]
        title_time = soup.select("div.item-content")[i].select("a")[1].text
         
        r_content =rq.get(url)
        soup_content = BeautifulSoup(r_content.text,"lxml")
        title.append(soup_content.find("span", "post-title").text)
        body.append("".join(str(x) for x in soup_content.select("div.entry-content p")))
        publish_time.append(title_time.split("|")[-1])
        print(soup_content.find("span", "post-title").text)
        time.sleep(1)
 
df = pd.DataFrame({"title":title, "body":body, "publish_time":publish_time})

print(df)