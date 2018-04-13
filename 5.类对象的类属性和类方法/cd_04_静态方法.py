class Dog(object):

    # 定义静态方法:不需要访问实例属性和调用实例方法,也不需要访问类属性和调用类方法
    @staticmethod
    def run():
        print("狗在跑...")

# 通过类名.调用静态方法
Dog.run()

