import matplotlib.pyplot as plt
import numpy as np
import data_get_7d as dg

# 获取数据
y1 = dg.get_high_tem()
for i in range(len(y1)):
    y1[i] = eval(y1[i])

y2 = dg.get_low_tem()
for i in range(len(y2)):
    y2[i] = eval(y2[i])

x=np.arange(0,36,5)
plt.figure(figsize=(10, 6))

# 设置字体以便显示中文
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 获取日期列表并设置x轴刻度标签
date_list = dg.get_date_list()
date_list2=dg.get_weather_list()
plt.xticks([0,5,10,15,20,25,30,35], date_list)
plt.yticks(np.arange(-20,25,1))

# 设置图表标题和轴标签
plt.xlabel('日期')
plt.ylabel('温度/℃')
plt.title('最高温度和最低温度折线图')

# 绘制图例
l1,=plt.plot(x,y1,color='red',label='high')
l2,=plt.plot(x,y2,color='blue',label='low')
plt.legend(handles=[l1,l2,],labels=['high','low'],loc='best')
# 绘制折线图和散点图
plt.plot(x, y1,color='red')
plt.scatter(x, y1,color='red')
for i, txt in enumerate(y1):
    plt.text(x[i], y1[i]+0.5, str(txt)+'℃', fontsize=11,color='red') # 在散点上方0.5的位置标注数字

plt.plot(x, y2,color='blue')
plt.scatter(x, y2,color='blue')
for i, txt in enumerate(y2):
    plt.text(x[i], y2[i]+0.5, str(txt)+'℃', fontsize=11,color='blue')  # 在散点上方0.5的位置标注数字
    plt.text(x[i],y2[i]+2,date_list2[i],fontsize=12,color='black')

# 显示网格线
plt.grid(True)
# 显示图形
plt.show()