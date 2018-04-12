class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")

class Dog(Animal):
    def bark(self):
        print("汪汪叫...")

# XiaoTianQuan类拥有Dog类和Animal类的所有属性与方法
# 子类拥有父类以及父类的父类的所有属相和方法
class XiaoTianQuan(Dog):
    def fly(self):
        print("飞起来..")

class Cat(Animal):
    def catch(self):
        print("抓老鼠...")

# 创建哮天犬对象
xiaotianquan = XiaoTianQuan()
xiaotianquan.eat()
xiaotianquan.bark()
xiaotianquan.fly()

# 创建猫对象
mao = Cat()
mao.catch()





