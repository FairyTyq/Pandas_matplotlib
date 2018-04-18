#coding:utf-8
import pandas
from matplotlib import pyplot as plt

'''
代码提示：
1.使用Pandas读取JSON文件数据
2.获取重复的用户ID数据
3.求解每位用户的总学习时长
4.绘制线型图
5.设置图标题及坐标轴名称
'''

def data_plot():
    f_data = pandas.read_json('/home/shiyanlou/Code/user_study.json')
    data = f_data[['user_id','minutes']].groupby('user_id').sum()
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title('StudyData')
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    ax.plot(data)
    plt.show()

    return ax

#data_plot()

