# mpl_cn_font

## 项目简介

`mpl_cn_font` 是一个用于简化 Matplotlib 中文字体配置的 Python 包。它提供了自动字体配置和灵活的字体切换功能，让你在绘图时轻松显示中文字符。

## 特性

- 自动配置：导入即可自动配置默认中文字体
- 灵活切换：支持多种中文字体动态切换
- 简单易用：提供简洁的 API 接口
- 开箱即用：字体文件随包安装，无需额外下载

## 安装

使用 pip 安装：

```bash
pip install .
```

或者从 GitHub 安装：

```bash
pip install git+https://github.com/ZongwuWang/mpl_cn_font.git
```

## 快速开始

### 基本使用

导入包后会自动配置 SimHei 字体：

```python
import mpl_cn_font
import matplotlib.pyplot as plt

# 现在可以正常显示中文
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("示例图表")
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.show()
```

### 切换字体

使用 `set_font()` 函数切换不同的中文字体：

```python
import mpl_cn_font

# 切换到 SimSun 字体
mpl_cn_font.set_font('SimSun')

# 切换到 KaiTi 字体
mpl_cn_font.set_font('KaiTi')
```

### 查看可用字体

```python
import mpl_cn_font

# 获取所有可用字体列表
fonts = mpl_cn_font.get_available_fonts()
print("可用字体:", fonts)
```

## API 参考

### set_font(font_name='SimHei')

设置 Matplotlib 的默认中文字体。

**参数：**
- `font_name` (str): 字体名称，默认为 'SimHei'

**返回值：**
- `bool`: 设置成功返回 True，失败返回 False

**示例：**

```python
import mpl_cn_font

# 使用黑体
mpl_cn_font.set_font('SimHei')

# 使用宋体
mpl_cn_font.set_font('SimSun')
```

### get_available_fonts()

获取所有可用的字体列表。

**返回值：**
- `List[str]`: 可用字体名称列表

**示例：**

```python
import mpl_cn_font

fonts = mpl_cn_font.get_available_fonts()
print(fonts)  # ['KaiTi', 'SimHei', 'SimSun', ...]
```

## 支持的字体

将字体文件（.ttf格式）放在 `src/mpl_cn_font/fonts/` 目录下即可自动识别。

常用中文字体：
- **SimHei** (黑体) - 默认字体
- **SimSun** (宋体)
- **KaiTi** (楷体)
- **Microsoft YaHei** (微软雅黑)
- 等等...

## 文件结构

```
mpl_cn_font/
├── src/
│   └── mpl_cn_font/
│       ├── __init__.py          # 包初始化，导出公共API
│       ├── font_manager.py      # 字体管理核心模块
│       └── fonts/               # 字体文件目录
│           ├── SimHei.ttf
│           ├── SimSun.ttf
│           └── ...
├── pyproject.toml               # 项目配置文件
├── setup.cfg
└── README.md
```

## 工作原理

1. **自动初始化**：导入包时自动调用 `init_default_font()` 配置 SimHei 字体
2. **字体注册**：使用 `matplotlib.font_manager.addfont()` 注册字体文件
3. **配置更新**：修改 `plt.rcParams` 设置字体优先级
4. **缓存清理**：可选清理 matplotlib 字体缓存以确保更新生效

## 常见问题

### Q: 为什么设置字体后还是显示方框？

A: 请确保：
1. 字体文件(.ttf)存在于 `src/mpl_cn_font/fonts/` 目录
2. 字体文件是完整有效的（不是占位符文件）
3. 重启 Python 解释器或清理 matplotlib 缓存

### Q: 如何添加新字体？

A: 将 .ttf 字体文件复制到 `src/mpl_cn_font/fonts/` 目录，重新安装包即可：

```bash
# 复制字体文件
cp MyFont.ttf src/mpl_cn_font/fonts/

# 重新安装
pip install . --force-reinstall
```

### Q: 字体文件在哪里可以获取？

A: 可以从以下途径获取字体：
- 系统字体目录（Windows: `C:\Windows\Fonts`, macOS: `/Library/Fonts/`）
- Google Fonts、Adobe Fonts 等字体网站
- GitHub 上的开源字体项目

注意版权问题，仅使用授权允许的字体。

## 贡献

欢迎贡献！请提交 Issue 或 Pull Request。

## 许可证

MIT License - 详见 LICENSE 文件