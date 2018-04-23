# -*- coding: utf-8 -*-
# @ProjectName: Python_面向对象
# @FileName: cd_03_文件打开方式&写入&追加数据.py
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-23 15:35

# open() 函数默认是以 只读的方式 打开文件,并返回文件对象
# open() 语法格式: f = open("文件名","访问方式")
# 访问方式: r:只读 w:只写 a:追加 r+:读写 w+:读写 a+:读写
# 实际开发中更多的会以 只读,只写 的方式操作文件

### 练习示例: 向README文件中添加内容 usename
# 新写入的内容会覆盖文件中之前的内容
# f = open("README","w")

# 新写入的内容会在文件中内容的最后面追加内容
f = open("README","a")

f.write("username")

f.close()








