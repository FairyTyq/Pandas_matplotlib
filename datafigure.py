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
    # 读取json文件中的数据
    f_data = pandas.read_json('/home/shiyanlou/Code/user_study.json')
    # 按照user_id分组，并对minutes求和
    data = f_data[['user_id','minutes']].groupby('user_id').sum()
    # 创建一个figure对象
    fig = plt.figure()
    # 添加坐标轴，以及坐标轴的title，以及x轴，y轴的信息
    ax = fig.add_subplot(1,1,1)
    ax.set_title('StudyData')
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    # 在坐标轴上按plot方式描绘数据
    ax.plot(data)
    # 显示图形
    plt.show()

    return ax

#data_plot()

