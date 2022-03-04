class Score():  # 分数输入类
    def __init__(self,result):
        try:
            self.result = int(result)
        except:
            print("输入非字符串")

    def setScore(self):
        try:
            if 0 <= self.result <= 100:
                print("成绩输入成功：",self.result)
            else:
                print("超出正常值,成绩为0")
                self.result = 0
        except:
            print("输入错误,成绩为0")
            self.result = 0


    def getScore(self):
        return self.result



