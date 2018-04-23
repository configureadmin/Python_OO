# -*- coding: utf-8 -*-
# @ProjectName: Python_面向对象
# @FileName: cd_02_文件操作的函数与方法.py
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-23 15:10

### 文件的操作套路非常固定,一般分为三个步骤
# 1.打开文件
# 2.读/写文件
#   读:将文件内容读入内存
#   写:将内存内容写入文件
# 3.关闭文件

# open() 函数负责打开文件,并且返回 文件对象
# read()/write()/close() 三个方法都需要 文件对象 来调用

### 示例:读取文件
# 打开文件
file = open("README")
# 读取文件内容
text = file.read()
print(text)

print("*"*20)
# 文件在第一次执行读取后read(),文件指针会发送变化,在文件的最末尾,所以第二次读取不会再读取到内容
t = file.read()
print(t)

# 关闭文件
file.close()





