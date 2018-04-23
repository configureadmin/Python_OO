# -*- coding: utf-8 -*-
# @ProjectName: Python_面向对象
# @FileName: cd_05_小文件的读写案例(复制文件).py
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-23 15:54

# 打开两个文件
file_read = open("README")
file_write = open("README[复制]","w")

# 先读取 file_read 文件的内容
text = file_read.read()

# 把读取到text中内容写入到file_write文件中
file_write.write(text)

file_read.close()
file_write.close()
