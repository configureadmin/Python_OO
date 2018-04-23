# -*- coding: utf-8 -*-
# @ProjectName: Python_面向对象
# @FileName: cd_02_from_import局部导入.py
# @Desc: 从一个模块中局部导入部分工具
# @Author: Administrator
# @Date: 2018-04-23 10:41

# import :是一次性把 模块中的 所有工具全部导入 ,并通过 模块名/别名 访问
# from 模块名 import 工具名 :是从模块中 导入 部分工具,可以直接使用模块提供的工具 :全局变量 ,函数 ,类

# 注意:如果导入的两个模块存在同名的函数,那么后导入模块的函数 会覆盖先导入模块的函数

# 使用from 模块名 import 工具名时也可以给工具起别名:格式如下
# from 模块名 import 工具名 as 别名

# from 模块名 import * : 也可以一次性导入模块的所有工具,但是不推荐使用,如果出现同名函数,出现问题不容易排查

from 测试模块一 import Dog
from 测试模块二 import Cat
from 测试模块一 import show
from 测试模块二 import show

dog = Dog()
print(dog)

cat = Cat()
print(cat)

# 两个模块都导入了show函数,后导入的会覆盖先导入的
show()

