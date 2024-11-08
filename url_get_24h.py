import requests
import re

url_24h='https://weather.cma.cn/web/weather/54161.html'
headers = { 
   "User-Agent":
       """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32"""}
url_page=requests.get(url=url_24h,headers=headers)

short_url_page=re.findall('<table class="hour-table" id="hourTable_0" style="">(.*?)</table>',url_page.text,re.S)

#下载文件
with open('weather_24h.txt','w',encoding='ISO-8859-1') as f:
    f.write(short_url_page[0])

print('24小时天气信息已经下载到weather_24h.txt文件中')