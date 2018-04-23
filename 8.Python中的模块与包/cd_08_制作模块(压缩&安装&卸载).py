# -*- coding: utf-8 -*-
# @ProjectName: Python_面向对象
# @FileName: cd_08_制作模块(压缩&安装&卸载).py
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-23 14:31

### 制作模块压缩包步骤
# 1.创建setup.py文件
# 2.构建模块: python3 setup.py build
# 3.生成发布压缩包: python3 setup.py sdist
### 结果是一个tar.gz 压缩包


### 安装模块
# tar -zxvf xxx.tar.gz
# sudo python3 setup.py install

### 卸载压缩包
# 直接在安装的目录下,把安装模块的目录删除掉
# sudo rm -r xxx

