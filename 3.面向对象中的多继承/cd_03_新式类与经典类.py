# 新式类:以object为基类的类
# 经典类:不以object为基类的类

# Python3.x 默认使用object作为基类
# Python2.x 则不会以object作为基类:需要继承 如下:
class A(object):
    pass

# 注意:为了保证编写代码能在同时在Python2.x和Python3.x上运行!!!
# 在定义类时,如果没有父类,建议统一继承自object
class 类名(object):
    pass


