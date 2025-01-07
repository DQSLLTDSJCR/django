from django.http import JsonResponse
from django.shortcuts import render
import requests

class Neko:
    def __init__(self, url,name,source,href):
        self.url = url
        self.name = name
        self.source = source
        self.href = href

    def getterurl(self):
        return self.url
    def getname(self):
        return self.name
    def getsource(self):
        return self.source
    def gethref(self):
        return self.href

    def setterurl(self,url):
        self.url = url
    def setname(self,name):
        self.name = name
    def setsource(self,source):
        self.source = source
    def sethref(self,href):
        self.href = href

def get_neko_image(request):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    # 获取图片 URL
    resp = requests.get("https://nekos.best/api/v2/neko", headers=headers, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    result=data["results"][0]
    neko = Neko(result["url"],result["artist_name"],result["source_url"],result["artist_href"])
    return render(request, 'neko/neko.html', {"image_url": neko.getsource(),"name":neko.getname(),"href":neko.gethref()})


