from bs4 import BeautifulSoup
import re

def get_date_m(data)->list:    #获取日期列表
    with open(f"weather_{data}.txt", "r", encoding="utf-8") as f:
        data = f.read()
    soup = BeautifulSoup(data, "lxml")

    date_m = soup.find_all("div",attrs={'class':'th200'})
    for i in range(len(date_m)):
        date_m[i] = date_m[i].string
        date_m[i]=re.findall(r'\d{4}-\d{2}-\d{2}',date_m[i])[0]
    return date_m

def get_tem_list(data)->list:   #获取温度列表
    with open(f"weather_{data}.txt", "r", encoding="utf-8") as f:
        data = f.read()
   
    tem_list=re.findall(r'<div class="th140">(-?\d{1,2})℃</div>',data)
    return tem_list

def get_high_tem(data)->list:   #获取最高温度列表
    high_tem=[]
    tem=get_tem_list(data)
    for i in range(len(tem)):
        if i%2==0:
            high_tem.append(tem[i])
    return high_tem

def get_low_tem(data)->list:    #获取最低温度列表      
    low_tem=[]
    tem=get_tem_list(data)
    for i in range(len(tem)):
        if i%2==1:
            low_tem.append(tem[i])
    return low_tem

if __name__ == '__main__':
    data=202406
    print(get_date_m(data))
    print(get_tem_list(data))
    print(get_high_tem(data))
    print(len(get_low_tem(data)))