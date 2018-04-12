# 定义一个猫类
class Cat:

    def eat(self):
        # 哪一个对象调用的方法,self就是哪个对象的引用
        print("%s爱吃鱼..."% self.name)

    def drink(self):
        print("%s爱喝水..."% self.name)

# 创建猫类对象
tom1 = Cat()
# 不建议使用此种方法给对象添加属性
tom1.name = "Tom"

tom2 = Cat()
# 不建议使用此种方法给对象添加属性
tom2.name = "懒猫"

tom1.eat()
tom1.drink()

tom2.eat()
tom2.drink()

print(tom1)
print(tom2)

addr1 = id(tom1)
addr2 = id(tom2)

print("%d"% addr1)  # 表示十进制输出数字
print("%x"% addr1)  # 表示十六进制输出数字
print("%d"% addr2)  # 表示十进制输出数字
print("%x"% addr2)  # 表示十六进制输出数字









