import matplotlib.pyplot as plt
import numpy as np
import get_date_m as gm
#设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10, 8))
# 设置标题
plt.suptitle('2023年10月-2024年9月最高温度和最低温度折线图')
# 绘制折线图
for a in range(10,13):
    plt.subplot(3, 4, a-9)
    data = 202300+a
    time = gm.get_date_m(data)
    x = np.arange(1,len(time)+1)
    h_tem = gm.get_high_tem(data)
    l_tem = gm.get_low_tem(data)
    # 改变数据类型
    h_tem = [float(t.replace('℃', '')) for t in h_tem]
    l_tem = [float(t.replace('℃', '')) for t in l_tem]
    plt.title(str(2023)+'-'+str(a))
    plt.plot(x, h_tem, 'r')
    plt.plot(x, l_tem, 'b')
    plt.grid()
for i in range(1,10):
    plt.subplot(3, 4, i+3)
    data = 202400+i
    time = gm.get_date_m(data)
    x = np.arange(1,len(time)+1)
    h_tem = gm.get_high_tem(data)
    l_tem = gm.get_low_tem(data)
    # 改变数据类型
    h_tem = [float(t.replace('℃', '')) for t in h_tem]
    l_tem = [float(t.replace('℃', '')) for t in l_tem]
    plt.title(str(2024)+'-'+str(i))
    plt.plot(x, h_tem, 'r')
    plt.plot(x, l_tem, 'b')
    plt.grid()
# 调整子图之间的间距
plt.tight_layout()
plt.show()
