class A:
    def test(self):
        print("test 方法...")

class B:
    def demo(self):
        print("demo 方法...")

# 多继承可以让子类对象同时具有多个父类的属性和方法
class C(A,B):
    pass

# 创建子类对象
c = C()
c.test()  # A类中的方法
c.demo()  # B类中的方法





