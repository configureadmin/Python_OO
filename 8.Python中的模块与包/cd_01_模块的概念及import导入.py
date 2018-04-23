# -*- coding: utf-8 -*-
# @ProjectName: Python_面向对象
# @FileName: cd_01_模块的概念及import导入.py
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-23 10:21

# 模块的导入方式(推荐使用)
# import 模块名一
# import 模块名二

# 还可以给导入的模块起别名:格式如下
# import 模块名 as 别名
# 注意:别名应该是大驼峰命名法

# 模块导入后的使用
# 通过 模块名. 使用模块提供的工具: 全局变量 ,函数 ,类

import 测试模块一
import 测试模块一 as DogModule
import 测试模块二
import 测试模块二 as CatModule

测试模块一.show()
测试模块二.show()

DogModule.show()
CatModule.show()

dog1 = 测试模块一.Dog()
dog2 = DogModule.Dog()
print(dog1)
print(dog2)

cat1 = 测试模块二.Cat()
cat2 = CatModule.Cat()
print(cat1)
print(cat2)