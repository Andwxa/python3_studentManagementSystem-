class Subject():
    def __init__(self):
        self.new_name = None
        self.new_ke = None
    def get_new_ke(self):
        return self.new_ke
    def get_new_name(self):
        return self.new_name
    def set_new_ke(self):
        self.new_ke = input("请输入老师所教的课程名称：")
    def set_new_name(self):
        self.new_name = input("请输入任课老师的姓名：")