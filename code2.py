import numpy as np
import matplotlib.pyplot as plt

# 生成连续信号
t_continuous = np.linspace(0, 10, 1000)
continuous_signal = np.sin(2 * np.pi * t_continuous)  # 以正弦信号为例

# 生成离散信号
t_discrete = np.arange(0, 10, 0.1)
discrete_signal = np.sin(2 * np.pi * t_discrete)  # 以正弦信号为例

# 绘制图形
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t_continuous, continuous_signal)
plt.title('Continuous Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.stem(t_discrete, discrete_signal, 'r')
plt.title('Discrete Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
