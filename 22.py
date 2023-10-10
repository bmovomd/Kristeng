import numpy as np
import matplotlib.pyplot as plt
n = np.arange(-5, 6)  
x = np.zeros_like(n)
x[len(n) // 2] = 1  
plt.stem(n, x, use_line_collection=True)
plt.xlabel('时间')
plt.ylabel('幅度')
plt.title('单位冲激信号')
plt.grid(True)
plt.show()
