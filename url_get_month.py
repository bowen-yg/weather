from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import re

def get_data(data):
    #创建浏览器选项对象
    options=Options()
    options.add_experimental_option('excludeSwitches',['enable-automation'])    # 以开发者模式启动
    options.add_experimental_option('useAutomationExtension',False) # 禁用扩展插件
    options.add_argument('--inprivate') # 无痕模式
    options.add_argument('--disable-sync')  # 禁用同步功能
    options.add_argument('--disable-features=EdgeSigninInterception,msEdgeAccountSwitching,msEdgeHybridAuth')  # 禁用账户相关特性
    options.add_argument('--disable-save-password-bubble')  # 禁用密码保存提示框
    options.add_argument('--ignore-certificate-errors')  # 忽略证书错误
    #创建浏览器操作对象
    path=r'C:/software/Driver_Notes/msedgedriver.exe'   # 浏览器驱动路径
    service=Service(executable_path=path)
    browser=webdriver.Edge(service=service,options=options)
    #访问网址
    url=f'https://lishi.tianqi.com/changchun/{data}.html'
    browser.implicitly_wait(15)   # 隐式等待最长时间
    # 访问网址
    browser.get(url)    
    time.sleep(3)
    print(browser.title)
    # 获取元素
    elecment=browser.find_element(By.CLASS_NAME,value='lishidesc2')
    elecment.click() # 点击
    time.sleep(3)

    url_page=browser.page_source
    url_page=re.findall(r'<ul class="thrui">(.*?)</ul>',url_page,re.S)[0]
    # 保存数据
    with open(f'weather_{data}.txt','w',encoding='utf-8') as f:
        f.write(url_page)
    time.sleep(3)


if __name__ == '__main__':
    for i in range(202410,202411):
        get_data(str(i))