import requests
import re
#请求头
headers = { 
   "User-Agent":
       """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32"""}
#网页链接，未来七天天气
url_7d='https://tianqi.2345.com/seventh-54161.htm'
#爬取七天天气
def seven_day_weather(url):
    url_page=requests.get(url=url,headers=headers)
    return url_page

url_page=seven_day_weather(url_7d)
#截取网页源码
short_url_page=re.findall(r'<div class="seven-day">(.+?)</div>',url_page.text,re.S)[0]
#写入文件
with open('weather_7d.txt','w',encoding='utf-8') as f:
    f.write(short_url_page)

print('七天天气信息已经下载到weather_7d.txt文件中')