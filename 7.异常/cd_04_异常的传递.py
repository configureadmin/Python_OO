# -*- coding: utf-8 -*-
# @ProjectName: Python_面向对象
# @FileName: cd_04_异常的传递.py
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-23 9:17

def demo1():
    return int(input("请输入一个整数: "))

def demo2():
    return demo1()

# 利用异常的传递性,在主程序中捕获异常
try:
    print(demo2())
except Exception as result:
    print("未知错误 %s"%result)

