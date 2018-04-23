# -*- coding: utf-8 -*-
# @ProjectName: Python_面向对象
# @FileName: cd_04___name__模块.py
# @Desc: 与 cd_05___name__模块导入.py 配合使用
# @Author: Administrator
# @Date: 2018-04-23 11:15

# 全局变量, 函数, 类
# 注意: 直接执行的代码不是向外界提供的工具!!!
def show():
    print("你好啊...")

# 如果直接执行此模块, __name__ 属性的值永远都是 __main__
if __name__ == "__main__":
    print(__name__)
    # 文件导入时,能够直接执行的代码不需要被执行
    print("某人开发的模块...")
    show()