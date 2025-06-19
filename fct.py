import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
import matplotlib
from matplotlib.ticker import ScalarFormatter

import seaborn as sns

# 从Excel文件读取数据
name = 'lowar'
file_path = 'data/' + name + '.xlsx'  # 请确保文件路径正确
df = pd.read_excel(file_path, sheet_name='Sheet1')

# 设置图形风格和字体
plt.rcParams['font.family'] = ['Arial Unicode MS', 'Heiti TC', 'PingFang SC', 'STHeiti']
plt.rcParams['font.sans-serif'] = plt.rcParams['font.family']

fig, ax1 = plt.subplots(1, 1, figsize=(8, 6))

# 过滤掉 NaN 值
for algo in [a for a in df['算法选择'].unique() if pd.notna(a)]:
    if algo != '无损网络':
        subset = df[df['算法选择'] == algo]
        ax1.plot(subset['丢包率'], subset['FCT'], 'o-', label=algo)

ax1.set_xscale('log')
ax1.set_xlabel('丢包率 (log scale)')
ax1.set_ylabel('平均FCT (ns)')
ax1.set_title('不同算法在不同丢包率下的FCT对比')
ax1.legend()
ax1.grid(True, which="both", ls="--")

# 设置纵坐标为科学计数法
ax1.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
# 或者使用 ScalarFormatter 更精确控制
# formatter = ScalarFormatter(useMathText=True)
# formatter.set_scientific(True)
# formatter.set_powerlimits((0, 0))
# ax1.yaxis.set_major_formatter(formatter)

plt.tight_layout()

# 保存图片到本地（支持 PNG、PDF、SVG、JPG 等格式）
output_path = "output/fct_" + name + '.png'  # 可以修改路径和文件名
plt.savefig(output_path, dpi=300, bbox_inches='tight')  # dpi 控制分辨率，bbox_inches='tight' 防止裁剪
print(f"图片已保存至：{output_path}")

plt.show()  # 仍然显示图片（可选）