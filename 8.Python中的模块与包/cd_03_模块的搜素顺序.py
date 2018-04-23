# -*- coding: utf-8 -*-
# @ProjectName: Python_面向对象
# @FileName: cd_03_模块的搜素顺序.py
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-23 11:00

# Python解释器在 导入模块时 ,会:
# 1.搜索当前目录 指定的 模块名的文件,如果有就直接导入
# 2.如果没有就搜索 系统目录
# 注意:开发时给文件起名,不要和系统的模块文件重名
# Python中每个模块都有一个内置属性__file__,可以查看模块的完整路径

# 示例如下,在当前目录下新建议个 random.py 文件
import random

print(random.__file__)
# ran = random.randint(1,5)
# print(ran)

# 示例结果:
# 当 当前目录下存在于系统同名的模块时,程序无法正常运行
# Python 解释器只会加载当前目录下的random.py文件,而不会加载系统的 ramdom 模块



