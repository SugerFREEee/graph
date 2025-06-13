import matplotlib.pyplot as plt
import numpy as np

# 数据准备
methods = ['FAST', 'STL_S', 'STL_S_G', 'Origin_S_G', 'RF', 'SVR']

cpu_data = {
    'RMSE': [1.38, 1.62, 1.81, 1.84, 1.88, 1.90],
    'R2': [0.68, 0.55, 0.44, 0.42, 0.39, 0.38]
}

memory_data = {
    'RMSE': [0.15, 0.22, 0.19, 0.18, 0.19, 0.19],
    'R2': [0.82, 0.60, 0.70, 0.75, 0.70, 0.70]
}

# 设置图形风格和字体
plt.rcParams['font.family'] = ['Arial Unicode MS', 'Heiti TC', 'PingFang SC', 'STHeiti']
plt.rcParams['font.sans-serif'] = plt.rcParams['font.family']

# 创建图表
plt.figure(figsize=(14, 10))

# CPU负载图表
plt.subplot(2, 2, 1)
plt.bar(methods, cpu_data['RMSE'], color='skyblue')
plt.title('CPU负载 - RMSE比较')
plt.ylabel('RMSE')
plt.ylim(1.2, 2.0)
for i, v in enumerate(cpu_data['RMSE']):
    plt.text(i, v+0.02, str(v), ha='center')

plt.subplot(2, 2, 2)
plt.bar(methods, cpu_data['R2'], color='lightgreen')
plt.title('CPU负载 - R²比较')
plt.ylabel('R²')
plt.ylim(0.3, 0.8)
for i, v in enumerate(cpu_data['R2']):
    plt.text(i, v+0.01, str(v), ha='center')

# 内存负载图表
plt.subplot(2, 2, 3)
plt.bar(methods, memory_data['RMSE'], color='skyblue')
plt.title('内存负载 - RMSE比较')
plt.ylabel('RMSE')
plt.ylim(0.1, 0.25)
for i, v in enumerate(memory_data['RMSE']):
    plt.text(i, v+0.005, str(v), ha='center')

plt.subplot(2, 2, 4)
plt.bar(methods, memory_data['R2'], color='lightgreen')
plt.title('内存负载 - R²比较')
plt.ylabel('R²')
plt.ylim(0.5, 0.9)
for i, v in enumerate(memory_data['R2']):
    plt.text(i, v+0.01, str(v), ha='center')

plt.tight_layout()
plt.show()