class Tools(object):

    # 使用赋值语句定义类属性,记录所有工具对象的数量
    count = 0
    def __init__(self,name):
        self.name = name
        #让类属性值 +1
        Tools.count += 1

# 创建工具对象
too1 = Tools("斧头")
too2 = Tools("砍刀")
too3 = Tools("弓箭")

print(Tools.count)



