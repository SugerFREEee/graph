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

# 图1: FCT和吞吐量对比
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# FCT对比
for algo in df['算法选择'].unique():
    if algo != '无损网络':
        subset = df[df['算法选择'] == algo]
        if not subset.empty:  # 确保有数据
            ax1.plot(subset['丢包率'], subset['FCT(ns)'], 'o-', label=algo)
ax1.set_xscale('log')
ax1.set_xlabel('丢包率 (log scale)')
ax1.set_ylabel('FCT (ns)')
ax1.set_title('FCT对比')
ax1.legend()
ax1.grid(True, which="both", ls="--")

# 吞吐量对比
for algo in df['算法选择'].unique():
    if algo != '无损网络':
        subset = df[df['算法选择'] == algo]
        if not subset.empty:  # 确保有数据
            ax2.plot(subset['丢包率'], subset['吞吐量(B/ns)'], 'o-', label=algo)
ax2.axhline(y=lossless_throughput, color='r', linestyle='--', label='无损网络')
ax2.set_xscale('log')
ax2.set_xlabel('丢包率 (log scale)')
ax2.set_ylabel('吞吐量 (B/ns)')
ax2.set_title('吞吐量对比')
ax2.legend()
ax2.grid(True, which="both", ls="--")

plt.tight_layout()

# 保存图片到本地（支持 PNG、PDF、SVG、JPG 等格式）
output_path = "output/throughput_" + name + '.png'  # 可以修改路径和文件名
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # dpi 控制分辨率，bbox_inches='tight' 防止裁剪
print(f"图片已保存至：{output_path}")

plt.show()
