"""
字体管理模块，负责加载和配置matplotlib的中文字体
"""
from pathlib import Path
from typing import List, Optional
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


def get_fonts_dir() -> Path:
    """获取包内字体目录"""
    return Path(__file__).parent / 'fonts'


def get_available_fonts() -> List[str]:
    """
    获取所有可用的字体列表

    Returns:
        可用字体名称列表（不包含.ttf扩展名）
    """
    fonts_dir = get_fonts_dir()
    if not fonts_dir.exists():
        return []

    fonts = []
    for font_file in fonts_dir.glob('*.ttf'):
        fonts.append(font_file.stem)

    return sorted(fonts)


def get_font_path(font_name: str) -> Optional[Path]:
    """
    获取指定字体的路径

    Args:
        font_name: 字体名称（不包含.ttf扩展名）

    Returns:
        字体文件路径，如果不存在则返回None
    """
    fonts_dir = get_fonts_dir()
    font_path = fonts_dir / f'{font_name}.ttf'

    if font_path.exists():
        return font_path
    return None


def register_font(font_name: str) -> bool:
    """
    将字体注册到matplotlib的字体管理器

    Args:
        font_name: 字体名称

    Returns:
        注册是否成功
    """
    font_path = get_font_path(font_name)
    if font_path is None:
        return False

    try:
        # 将字体文件添加到matplotlib的字体管理器
        fm.fontManager.addfont(str(font_path))
        return True
    except Exception as e:
        print(f"警告: 注册字体 {font_name} 失败: {e}")
        return False


def set_font(font_name: str = 'SimHei') -> bool:
    """
    设置matplotlib的默认中文字体

    Args:
        font_name: 字体名称，默认为'SimHei'

    Returns:
        设置是否成功
    """
    # 检查字体是否存在
    font_path = get_font_path(font_name)
    if font_path is None:
        available_fonts = get_available_fonts()
        print(f"错误: 字体 '{font_name}' 不存在")
        print(f"可用字体: {', '.join(available_fonts)}")
        return False

    # 注册字体
    if not register_font(font_name):
        print(f"错误: 无法注册字体 '{font_name}'")
        return False

    # 设置matplotlib的字体配置
    plt.rcParams['font.sans-serif'] = [font_name] + plt.rcParams['font.sans-serif']
    plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

    # 清除matplotlib字体缓存（可选）
    try:
        import shutil
        cache_dir = plt.get_cachedir()
        font_cache = Path(cache_dir) / 'fontlist-v330.json'
        if font_cache.exists():
            font_cache.unlink()
    except Exception:
        pass  # 忽略缓存清理错误

    print(f"已设置字体为: {font_name}")
    return True


def init_default_font(font_name: str = 'SimHei') -> None:
    """
    初始化默认字体（在包导入时自动调用）

    Args:
        font_name: 默认字体名称
    """
    set_font(font_name)
