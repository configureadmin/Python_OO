# 定义一个猫类
class Cat:
    """ 这个类文档"""
    def __init__(self):
        print("这是对象的初始化方法")
        # 在初始化的时候给对象设置一个属性并赋值
        self.name = "Tom"

    def eat(self):
        print("%s 爱吃鱼"%self.name)

# 使用类名()创建对象的时候,会自动调用初始化方法__init__
tom = Cat()
print(tom.name)
tom.eat()







