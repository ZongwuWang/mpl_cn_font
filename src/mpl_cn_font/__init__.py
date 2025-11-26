"""
mpl_cn_font - Matplotlib中文字体配置包

提供简单易用的中文字体配置功能，支持多种字体切换
"""

from .font_manager import (
    set_font,
    get_available_fonts,
    init_default_font
)

# 版本信息
__version__ = '0.1.0'
__author__ = 'Zongwu Wang'

# 导出的公共API
__all__ = [
    'set_font',
    'get_available_fonts',
]

# 包导入时自动初始化默认字体（SimHei）
init_default_font()