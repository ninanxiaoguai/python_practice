import requests
from bs4 import BeautifulSoup
import re
import urllib

def read(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    bs = BeautifulSoup(html,'html5lib')
    return bs

def get_url(url,number):
    bs = read(url)
    list_url = []
    for ul in  bs.find_all("a",title = re.compile("^新托福口语task{}".format(number))):
        list_url.append(ul.get("href"))
    return list_url

def write_html(url,number):
    bs = read(url)
    ul = bs.find_all("div", class_="mt40")
    title = bs.find_all("h1", class_="t2 show_t2")
    title = str(title).replace('[',"").replace(']',"")
    ul = str(ul).replace('[',"").replace(']',"")
    with open("task{}.txt".format(number), "a",encoding='utf-8') as f:
        f.write(title)
        f.write(ul)
        f.write("\n\n")

for num in range(1,7):
    su = "http://toefl.koolearn.com/kouyu/"
    list_url = get_url(su,num)
    for url in list_url:
        write_html(url,num)
        print(su," is ok")


for num in range(1,7):
    for i in range(2,350):
        su = "http://toefl.koolearn.com/kouyu/{}.html".format(i)
        list_url = get_url(su,num)
        for url in list_url:
            write_html(url,num)
            print(su," is ok")







