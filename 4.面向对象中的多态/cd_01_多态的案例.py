class Dog(object):
    def __init__(self,name):
        self.name = name
    def game(self):
        print("%s 蹦蹦跳跳的玩耍..."%self.name)

class XiaoTianQuan(Dog):
    def game(self):
        print("%s 飞到天上去玩耍!!!" %self.name)

class Person(object):
    def __init__(self,name):
        self.name = name
    def game_with_dog(self,dog):
        print("%s 与 %s 愉快的玩耍..."%(self.name,dog.name))
        # 让狗玩耍
        dog.game()

# 创建狗对象
# wangcai =  Dog("旺财")
wangcai = XiaoTianQuan("飞天旺财")
# 创建小明对象
xiaoming = Person("小明")
# 让小明调用跟狗玩的方法
xiaoming.game_with_dog(wangcai)

