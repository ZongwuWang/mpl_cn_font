"""
快速测试脚本
"""
import sys
sys.path.insert(0, '/home/wangzongwu/mpl_cn_font/mpl_cn_font/src')

import mpl_cn_font

print("测试1: 查看可用字体")
fonts = mpl_cn_font.get_available_fonts()
print(f"可用字体: {fonts}")

print("\n测试2: 设置字体")
result = mpl_cn_font.set_font('SimHei')
print(f"设置SimHei字体: {'成功' if result else '失败'}")

print("\n测试3: 尝试设置不存在的字体")
result = mpl_cn_font.set_font('NonExistentFont')
print(f"设置不存在的字体: {'成功' if result else '失败（预期）'}")

print("\n测试完成！")
