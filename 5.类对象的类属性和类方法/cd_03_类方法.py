class Tools(object):

    # 使用赋值语句定义类属性,记录所有工具对象的数量
    count = 0
    # 类方法:使用@classmethod标识,方法名后面需要加上cls
    @classmethod
    def show_tool_count(cls):
        print("工具对象的对象: %d" %cls.count)

    def __init__(self,name):
        self.name = name
        #让类属性值 +1
        Tools.count += 1



# 创建工具对象
too1 = Tools("斧头")
too2 = Tools("砍刀")

# 调用类方法
Tools.show_tool_count()

# 总结: 在类方法内部,可以使用cls访问类属性和调用类方法
