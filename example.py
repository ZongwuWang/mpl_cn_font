"""
mpl_cn_font 使用示例
"""
import mpl_cn_font
import matplotlib.pyplot as plt
import numpy as np


def example_basic():
    """基本使用示例 - 导入即可使用"""
    print("=" * 50)
    print("示例1: 基本使用（自动配置SimHei字体）")
    print("=" * 50)

    # 创建简单图表
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='正弦波')
    plt.title('中文标题测试')
    plt.xlabel('横轴')
    plt.ylabel('纵轴')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('example_basic.png', dpi=100)
    print("图片已保存为: example_basic.png\n")
    plt.close()


def example_switch_fonts():
    """字体切换示例"""
    print("=" * 50)
    print("示例2: 切换不同字体")
    print("=" * 50)

    # 获取可用字体
    fonts = mpl_cn_font.get_available_fonts()
    print(f"可用字体: {fonts}\n")

    # 创建多子图，展示不同字体
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('不同字体效果对比', fontsize=16)

    test_fonts = ['SimHei', 'SimSun', 'KaiTi', 'Microsoft YaHei']
    available_test_fonts = [f for f in test_fonts if f in fonts]

    for idx, font_name in enumerate(available_test_fonts[:4]):
        row = idx // 2
        col = idx % 2
        ax = axes[row, col]

        # 切换字体
        mpl_cn_font.set_font(font_name)

        # 绘制测试图表
        x = np.linspace(0, 2*np.pi, 50)
        y = np.sin(x)
        ax.plot(x, y, 'b-', linewidth=2)
        ax.set_title(f'{font_name} - 正弦函数图')
        ax.set_xlabel('角度（弧度）')
        ax.set_ylabel('正弦值')
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('example_fonts.png', dpi=100)
    print("图片已保存为: example_fonts.png\n")
    plt.close()


def example_complex_plot():
    """复杂图表示例"""
    print("=" * 50)
    print("示例3: 复杂图表（柱状图、折线图组合）")
    print("=" * 50)

    # 重置为默认字体
    mpl_cn_font.set_font('SimHei')

    # 创建数据
    categories = ['一月', '二月', '三月', '四月', '五月', '六月']
    sales = [120, 150, 180, 160, 200, 220]
    profit = [30, 45, 60, 50, 70, 85]

    x = np.arange(len(categories))
    width = 0.35

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # 柱状图
    bars = ax1.bar(x, sales, width, label='销售额', color='skyblue', alpha=0.8)
    ax1.set_xlabel('月份', fontsize=12)
    ax1.set_ylabel('销售额（万元）', fontsize=12)
    ax1.set_title('2024年上半年销售与利润分析', fontsize=14, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories)
    ax1.legend(loc='upper left')
    ax1.grid(True, alpha=0.3, axis='y')

    # 在柱状图上添加数值
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=9)

    # 折线图
    ax2 = ax1.twinx()
    line = ax2.plot(x, profit, 'ro-', linewidth=2, markersize=8, label='利润')
    ax2.set_ylabel('利润（万元）', fontsize=12)
    ax2.legend(loc='upper right')

    # 在折线图上添加数值
    for i, val in enumerate(profit):
        ax2.text(i, val+2, f'{val}', ha='center', fontsize=9)

    plt.tight_layout()
    plt.savefig('example_complex.png', dpi=100)
    print("图片已保存为: example_complex.png\n")
    plt.close()


if __name__ == '__main__':
    print("\n" + "="*50)
    print("mpl_cn_font 使用示例")
    print("="*50 + "\n")

    # 运行示例
    example_basic()
    example_switch_fonts()
    example_complex_plot()

    print("="*50)
    print("所有示例运行完成！")
    print("="*50)
