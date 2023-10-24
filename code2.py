import numpy as np
import matplotlib.pyplot as plt

def sawtooth(x):
    return 2 * (x - np.floor(x + 0.5))

# 生成离散的x坐标
x_discrete = np.arange(0, 10, 0.1)

# 计算离散的y坐标
y_discrete = sawtooth(x_discrete)

# 生成连续的x坐标
x_continuous = np.linspace(0, 10, 1000)

# 计算连续的y坐标
y_continuous = sawtooth(x_continuous)

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘制离散图形
plt.subplot(2, 1, 1)
plt.stem(x_discrete, y_discrete, linefmt='b-', markerfmt='bo', basefmt=' ')

plt.title('离散锯齿函数')
plt.xlabel('横坐标')
plt.ylabel('纵坐标')

# 绘制连续图形
plt.subplot(2, 1, 2)
plt.plot(x_continuous, y_continuous, 'b-')

plt.title('连续锯齿函数')
plt.xlabel('横坐标')
plt.ylabel('纵坐标')

# 显示图形
plt.tight_layout()
plt.show()
