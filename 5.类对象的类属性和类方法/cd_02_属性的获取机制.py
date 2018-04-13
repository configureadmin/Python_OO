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
# 工具的总数量
print("工具的总数量: %d" %Tools.count)
print("工具的总数量: %d" %too1.count)
print("工具的总数量: %d" %too2.count)


# 总结:要访问类属性的两种方式:
# 类名.类属性
# 对象.类属性(不推荐使用)

# 注意: 使用 对象.类属性 = 值 赋值语句,只会给对象添加一个属性,而不会影响到类属性的值


