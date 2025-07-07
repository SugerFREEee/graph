import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# 从Excel文件读取数据
name = 'flow'
file_path = 'data/' + name + '.xlsx'  # 请确保文件路径正确
df = pd.read_excel(file_path, sheet_name='Sheet1')

# 计算吞吐量下降百分比
lossless_throughput = df[df['算法选择'] == '无损网络']['吞吐量(B/ns)'].values[0]
df['吞吐量下降百分比'] = (1 - df['相较于无损网络']) * 100

# 设置图形风格和字体
plt.rcParams['font.family'] = ['Arial Unicode MS', 'Heiti TC', 'PingFang SC', 'STHeiti']
plt.rcParams['font.sans-serif'] = plt.rcParams['font.family']

font = 24

# 设置全局字体大小
plt.rcParams['axes.labelsize'] = font  # 坐标轴标签字体大小
plt.rcParams['xtick.labelsize'] = font  # x轴刻度标签字体大小
plt.rcParams['ytick.labelsize'] = font  # y轴刻度标签字体大小
plt.rcParams['legend.fontsize'] = font  # 图例字体大小

# 创建图形
fig, ax2 = plt.subplots(figsize=(8, 6))

# 吞吐量对比
for algo in df['算法选择'].unique():
    if algo != '无损网络':
        subset = df[df['算法选择'] == algo]
        if not subset.empty:  # 确保有数据
            ax2.plot(subset['丢包率'], subset['吞吐量(B/ns)'], 'o-', label=algo)
ax2.axhline(y=lossless_throughput, color='r', linestyle='--', label='Lossless network')
ax2.set_xscale('log')
ax2.set_xlabel('Loss rate', fontsize=font)
ax2.set_ylabel('Throughput (B/ns)', fontsize=font)
ax2.legend()
ax2.grid(True, which="both", ls="--")

plt.tight_layout()

# 保存图片到本地
output_path = "output/throughput_" + name + '.png'  # 可以修改路径和文件名
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"吞吐量对比图已保存至：{output_path}")

plt.show()