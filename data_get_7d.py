from bs4 import BeautifulSoup
import re

with open('weather_7d.txt','r',encoding='utf-8') as f:
    url_page=f.read()

soup=BeautifulSoup(url_page,'lxml')

def get_weather_list()->list:   #获取天气列表
    weather_list=soup.find_all('i',limit=8)
    for i in range(len(weather_list)):
        weather_list[i]=weather_list[i].string
    # weather_list.pop()
    return weather_list

def get_date_list()->list:  #获取日期列表
    date_list=soup.find_all('em')
    for i in range(len(date_list)):
        date_list[i]=date_list[i].string
    return date_list

def get_tem_list()->list:   #获取温度列表
    tem_list=soup.find_all('span','tem-show')
    for i in range(len(tem_list)):
        tem_list[i]=tem_list[i].string
    return tem_list

def get_wind_list()->list:  #获取风力列表
    wind_list=soup.find_all('span','wind-name')
    for i in range(len(wind_list)):
        wind_list[i]=wind_list[i].string
    return wind_list
def get_air_list()->list:   #获取空气质量列表
    air_list=soup.find_all('span','wea-qulity')
    for i in range(len(air_list)):
        air_list[i]=air_list[i].string
    return air_list

def get_high_tem():
    high_tem=[]
    tem_list=get_tem_list()
    for i in tem_list:
        high_tem.append(re.search(r'~(-?\d{1,2})°',i).group(1))
    return high_tem

def get_low_tem():
    low_tem=[]
    tem_list=get_tem_list()
    for i in tem_list:
        low_tem.append(re.match(r'(-?\d{1,2})~',i).group(1))
    return low_tem


if __name__ == '__main__':
    print(get_high_tem())
    print(get_low_tem())
    print(get_date_list())
    print(get_tem_list())
    print(get_weather_list())
    print(get_wind_list())
    print(get_air_list())