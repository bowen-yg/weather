import re

with open('weather_24h.txt', 'r',encoding='utf-8') as f:
    html = f.read()

def get_time_list()->list:  #获取时间列表
    time_list=re.findall(r'<td>(\d{1,2}:\d{1,2})</td>',html)
    return time_list

def get_tem_list()->list:   #获取温度列表
    tem_list=re.findall(r'<td>(-?\d{1,2}\.?\d?)℃</td>',html)
    return tem_list[:8]

def get_humidity_list()->list:   #获取湿度列表
    humidity_list=re.findall(r'<td>(\d{1,2}\.?\d?\%)</td>',html)
    return humidity_list[:8]

def get_cloud_list()->list:   #获取云量列表
    cloud_list=re.findall(r'<td>(\d{1,2}\.?\d?\%)</td>',html)
    return cloud_list[8:16]

def get_wind_list()->list:  #获取风速列表
    wind_list=re.findall(r'<td>(-?\d{1,2}\.?\d?m/s)</td>',html)
    return wind_list[:8]

if __name__ == '__main__':
    print(get_time_list())
    print(get_tem_list())
    print(get_wind_list())
    print(get_humidity_list())
    print(get_cloud_list())

# s=soup.find_all('td',string=re.compile(r"6.5"))
# print(s)
