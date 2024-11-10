import matplotlib.pyplot as plt
import data_get_24h as dg24
import numpy as np
#获取数据
y=dg24.get_tem_list()
for i in range(len(y)):
    y[i]=eval(y[i])
#设置字体
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

#设置刻度
x=np.arange(0,40,5)
plt.xticks(x,dg24.get_time_list())
plt.yticks(np.arange(-10,10,1))

#坐标轴标注
plt.xlabel('时间')
plt.ylabel('温度/℃')

#设置标题
plt.title('24小时气温变化图')

#绘制散点图
for i,txt in enumerate(y):
    plt.text(x[i],y[i]+0.5,str(txt)+'℃',fontsize=11)
    if y[i]>0:
        plt.scatter(x[i],y[i],color='red')
    else:
        plt.scatter(x[i],y[i],color='blue')

#显示网格线
plt.grid(True)

#绘制拟合曲线
fit=np.polyfit(x,y,deg=6)

x_new=np.linspace(min(x),max(x),100)
y_new=np.polyval(fit,x_new)

l1,=plt.plot(x_new,y_new,color='orange')

#显示图例
plt.legend(handles=[l1,],labels=['温度'],loc='best')

#显示图形
plt.show()