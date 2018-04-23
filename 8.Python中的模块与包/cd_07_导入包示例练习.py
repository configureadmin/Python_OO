# -*- coding: utf-8 -*-
# @ProjectName: Python_面向对象
# @FileName: cd_07_导入包示例练习.py
# @Desc: 案例演示
# @Author: Administrator
# @Date: 2018-04-23 14:08

### 练习示例:
# 1.新建一个 cd_message 包
# 2.在目录下新建两个文件 send_message 和 recrive_message
# 3.在send_message 文件中定义一个 send 函数
# 4.在receive_message 文件中定义一个 receive 函数
# 5.在外部直接导入 cd_message 包

# 导入cd_message包,要想再外界使用cd_message包的模块,需要在 __init__.py文件指定 对外界提供的模块
import cd_message

cd_message.send_message.send("aaa")
test = cd_message.receive_message.receive()
print(test)




