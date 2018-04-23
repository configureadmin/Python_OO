# -*- coding: utf-8 -*-
# @ProjectName: Python_面向对象
# @FileName: cd_04_使用readline分行读取大文件.py
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-23 15:46

# 打开文件
f = open("README")

while True:
    # 读取每一行的内容
    text = f.readline()
    # 判断是否读取到内容
    if not text:
        break
    # 每读取到一行的末尾 已经有了一个"\n"
    print(text,end="")

f.close()