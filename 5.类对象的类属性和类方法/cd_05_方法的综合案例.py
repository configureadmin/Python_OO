class Game(object):
    # 类属性:历史最高分
    top_score = 0

    # 对象初始化方法,实例属性
    def __init__(self,player_name):
        self.player_name = player_name

    # 静态方法
    @staticmethod
    def show_help():
        print("游戏帮助信息: 让僵尸进入大门")

     # 类方法
    @classmethod
    def show_top_score(cls):
        print("历史记录: %d" %cls.top_score)

    # 对象实例方法
    def start_game(self):
        print("%s 开始游戏啦..." % self.player_name)

# 查看游戏的帮助信息
Game.show_help()
# 查看游戏的历史最高分
Game.show_top_score()
# 创建游戏对象
game = Game("张三")
game.start_game()


# 总结:
# 实例方法内部访问实例属性
#     实例方法内部可以使用 类名.访问类属性
# 类方法内部访问类属性
# 静态方法内部既不访问实例属性也不访问类属性
#
# 注意:如果方法内部既要访问实力属性又要访问类属性,该方法应该怎么定义???
#     定义成实例方法




