# -*- coding: utf-8 -*-
# @ProjectName: Python_面向对象
# @FileName: cd_02_捕获未知错误.py
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-20 16:42

### 捕获未知错误
try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数: "))
    # 使用8除以输入的整数,并且输出
    result = 8 / num
    print(result)
except ValueError:
    print("请输入正确的整数")
except Exception as msg:
    print("未知错误: %s"%msg)
