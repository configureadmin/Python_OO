# -*- coding: utf-8 -*-
# @ProjectName: Python_面向对象
# @FileName: cd_06_大文件的读写案例(复制文件).py
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-23 16:14

# 打开两个文件
file_read = open("README")
file_write = open("README[复制]","w")

while True:
    # 读取每一行的内容
    text = file_read.readline()
    # 判断是否读取到内容
    if not text:
        break
    # 把读取到的每行内容写入到file_write文件中
    file_write.write(text)

file_read.close()
file_write.close()
