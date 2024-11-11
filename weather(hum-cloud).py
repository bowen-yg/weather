import matplotlib.pyplot as plt
import data_get_24h as dg24
#设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#提取数据
humidity=dg24.get_humidity_list()
cloud=dg24.get_cloud_list()
# 改变数据类型
cloud = [float(c.replace('%', '')) for c in cloud]
humidity = [float(h.replace('%', '')) for h in humidity]
#x、y轴以及图表名称
plt.xlabel('humidity (%)')
plt.ylabel('cloudy (%)')
plt.title('cloud-humidity relational scatter plot')
plt.grid()
#输出散点图
plt.scatter(humidity, cloud,s=125, alpha=0.3)
plt.show()