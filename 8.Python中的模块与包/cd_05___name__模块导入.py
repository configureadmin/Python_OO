# -*- coding: utf-8 -*-
# @ProjectName: Python_面向对象
# @FileName: cd_05___name__模块导入.py
# @Desc: 与 cd_04___name__模块.py 配合使用
# @Author: Administrator
# @Date: 2018-04-23 11:16

# 在导入文件时, 文件中 所有没有任何缩进的代码 都会执行一遍
import cd_04___name__模块

# 实际开发中,当前模块的测试代码 只在测试的情况下执行,而在被导入其他文件时,不被执行!!! __name__ 属性可以做到
# __name__ 是Python 解释器内置属性,记录着一个字符串
# 如果 是被其他文件导入的, __name__ 就是模块名
# 如果 是当前执行的程序, __name__ 就是 __main__

print("*" * 10)



### 开发中的实际情况
# 导入模块
# 定义全局变量
# 定义函数
# 定义类

# 在代码的最下方
def main():
    # 需要测试的代码
    pass

# 根据 __name__ 属性判断是否执行下方的代码
if __name__ == "__main__":
    main()