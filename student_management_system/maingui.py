# coding=utf-8 -*w*- -*x*- -*a*-
from tkinter import *
from tkinter import Entry
from tkinter.ttk import *
import tkinter as tk
import tkinter.messagebox
import os
from tkinter.ttk import Entry
# 学生成绩
from score import Score


class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title("学生管理系统")
        self.geometry("900x640+180+80")         # 主窗体大小：900宽 600高 ; 出现位置：180宽 80高
        self.resizable(False, False)            # 不可改变窗体大小
        self["bg"] = "skyblue"                  # 设置主体背景颜色为天蓝色
        # 加载gui
        self.setup_UI()                         # 子容器的加载
        # 开始时的加载数据
        self.all_student_list = []
        self.file_path = "Student.txt"
        self.load_file_student_info()           # 将数据取出来
        self.load_treeview(self.all_student_list)   # 放入TreeView中
        # 初始化搜索学号显示  创建列表和可变字符串
        self.query_result_list = []
        self.var_sno = StringVar()

    def setup_UI(self):
        # 设定样式
        self.Style01 = Style()
        self.Style01.configure("top.TPanedwindow", background="navy")
        self.Style01.configure("left.TPanedwindow")
        self.Style01.configure("right.TPanedwindow")
        self.Style01.configure("TButton", width=20, font=("黑体", 10))

        # 上边：标题区域,创建一个容器
        self.Pane_top = PanedWindow(width=900, height=90, style="top.TPanedwindow", orient=VERTICAL)
        self.Pane_top.place(x=0, y=0)
        # 左边：按钮区域,创建一个容器
        self.Pane_left = PanedWindow(width=200, height=540, style="left.TPanedwindow")
        self.Pane_left.place(x=0, y=94)
        # 右边：文本区域,创建一个容器
        self.Pane_right = PanedWindow(width=725, height=540, style="right.TPanedwindow")
        self.Pane_right.place(x=210, y=94)
        # 添加上边的标签
        Label_title = Label(self.Pane_top, text="学生管理系统", font=("黑体", 42), background="navy", foreground="white")
        Label_title.place(x=85, y=23)
        # 添加左边按钮
        self.Button_show = Button(self.Pane_left, text="显示所有信息", style="TButton", command=self.load_all_student)
        self.Button_show.place(x=20, y=20)
        self.Button_add = Button(self.Pane_left, text="添加学生信息", style="TButton", command=self.get_add_student)
        self.Button_add.place(x=20, y=50)
        self.Button_delete = Button(self.Pane_left, text="删除学生信息", style="TButton", command=self.get_del_student)
        self.Button_delete.place(x=20, y=80)
        self.Button_update = Button(self.Pane_left, text="修改学生信息", style="TButton", command=self.get_amend_studnet)
        self.Button_update.place(x=20, y=110)
        self.Button_statistics = Button(self.Pane_left, text="统计学生信息", style="TButton", command=self.get_Statistics_student)
        self.Button_statistics.place(x=20, y=140)
        self.Button_inquire = Button(self.Pane_left, text="查询学生信息", style="TButton", command=self.get_query_result)
        self.Button_inquire.place(x=20, y=170)
        self.Button_teacher = Button(self.Pane_left, text="课程管理界面", style="TButton", command=self.spik_teacher)
        self.Button_teacher.place(x=20, y=420)
        self.Button_again = Button(self.Pane_left, text="重新登陆", style="TButton", command=self.spik)
        self.Button_again.place(x=20, y=450)
        self.Button_out = Button(self.Pane_left, text="退出", style="TButton", command=self.usr_sign_quit)
        self.Button_out.place(x=20, y=480)

        # 添加右边上面
        self.LabelFrame_query = LabelFrame(self.Pane_right, text="学生信息查询", width=660, height=70)
        self.LabelFrame_query.place(x=10, y=10)
        # 添加控件
        self.Label_sno = Label(self.LabelFrame_query, text="学号：")
        self.Label_sno.place(x=5, y=13)
        self.Entry_sno = Entry(self.LabelFrame_query, width=15)
        self.Entry_sno.place(x=50, y=10)

        self.Label_name = Label(self.LabelFrame_query, text="姓名：")
        self.Label_name.place(x=175, y=13)
        self.Entry_name = Entry(self.LabelFrame_query, width=13)
        self.Entry_name.place(x=220, y=10)

        self.Label_python = Label(self.LabelFrame_query, text="python：")
        self.Label_python.place(x=330, y=13)
        self.Entry_python = Entry(self.LabelFrame_query, width=13)
        self.Entry_python.place(x=390, y=10)

        self.Label_c = Label(self.LabelFrame_query, text="C语言：")
        self.Label_c.place(x=495, y=13)
        self.Entry_c = Entry(self.LabelFrame_query, width=13)
        self.Entry_c.place(x=545, y=10)

        # 添加右下控件
        # 添加TreeView控件
        self.Tree = Treeview(self.Pane_right, columns=("sno", "names", "Python", "C"),show="headings", height=20)
        # 设置每一个列的宽度和对齐的方式
        self.Tree.column("sno", width=200, anchor="center")
        self.Tree.column("names", width=150, anchor="center")
        self.Tree.column("Python", width=150, anchor="center")
        self.Tree.column("C", width=156, anchor="center")
        # 设置每个列的标题
        self.Tree.heading("sno", text="学号")
        self.Tree.heading("names", text="姓名")
        self.Tree.heading("Python", text="Python")
        self.Tree.heading("C", text="C语言")
        self.Tree.place(x=10, y=80)

    # 退出的函数
    def usr_sign_quit(self):
        self.destroy()

    # 跳转回登录
    def spik(self):
        # 关闭当前页面
        self.usr_sign_quit()
        os.system("python login.py")

    # 跳转到课程管理
    def spik_teacher(self):
        # 关闭当前页面
        self.usr_sign_quit()
        # 加载新窗体
        os.system("python teacher.py")

    # 读取存入数组
    def load_file_student_info(self):
        if not os.path.exists(self.file_path):
            with open(file=self.file_path, mode="wb") as fd:
                sc = '1001,张三,61,61\n1002,李四,62,62\n1003,王五,63,63'
                fd.write(sc.encode())
            with open(file=self.file_path, mode="rb") as fd:
                # 一次读一行
                current_line = fd.readline()
                while current_line:
                    current_line = current_line.decode()    # 二进制转为str
                    temp_list = current_line.split(",")
                    self.all_student_list.append(temp_list)
                    # 读取下一行,读完了循环就结束了
                    current_line = fd.readline()
                print("文件读取出来的:", self.all_student_list)
        else:
            try:
                with open(file=self.file_path, mode="rb") as fd:
                    # 一次读一行
                    current_line = fd.readline()
                    while current_line:
                        current_line = current_line.decode()  # 二进制转为str
                        temp_list = current_line.split(",")
                        self.all_student_list.append(temp_list)
                        # 读取下一行,读完了循环就结束了
                        current_line = fd.readline()
                    print("文件里读取出来的:",self.all_student_list)
            except:
                tk.messagebox.showerror(title='警告', message='学生数据读取异常')

    # 将数组放入到树状列表中
    def load_treeview(self, current_list: list):
        # 判断是否有数据：
        if len(current_list) == 0:
            tk.messagebox.showerror(title='系统提示', message='文件里没有数据')
        else:
            for index in range(len(current_list)):
                self.Tree.insert("", index, values=(current_list[index][0], current_list[index][1],
                                                    current_list[index][2], current_list[index][3]))

    # 按照学号进行查询
    def get_query_result(self):
        self.sno = self.Entry_sno.get()
        if self.sno is None:
            tk.messagebox.showerror(title='警告', message='文本框不能为空')
        else:
            # TreeView中的内容清空
            for i in self.Tree.get_children():
                self.Tree.delete(i)
            # 准备查询条件：获取学号
            query_condition = self.Entry_sno.get()
            # 遍历List获取符合条件的学生信息
            for item in self.all_student_list:
                if query_condition in item[0]:
                    # 满足条件的学生
                    self.query_result_list.append(item)
            # 把结果加载的TreeView中
            self.load_treeview(self.query_result_list)
            # 将列表结果清除
            self.query_result_list.clear()

    # 显示所有信息
    def load_all_student(self):
        try:
            self.Tree.place(x=10, y=80)
            self.Tree_statistics.place_forget()
            # TreeView中的内容清空
            for i in self.Tree.get_children():
                self.Tree.delete(i)
            # 加载所有的学生信息到treeview
            self.load_treeview(self.all_student_list)
        except:
            # TreeView中的内容清空
            for i in self.Tree.get_children():
                self.Tree.delete(i)
            # 加载所有的学生信息到treeview
            self.load_treeview(self.all_student_list)

    # 添加学生信息
    def get_add_student(self):
        # 获得学号,姓名,python,c语言
        self.sno = self.Entry_sno.get()
        self.name = self.Entry_name.get()
        score = Score(self.Entry_python.get())  # 判断成绩
        score.setScore()
        self.python = str(score.getScore())
        score = Score(self.Entry_c.get())   # 判断成绩
        score.setScore()
        self.c = str(score.getScore())
        self.list1 = [self.sno, self.name, self.python, self.c]
        print(self.list1)
        if self.sno == "" or self.name == "" or self.python == "" or self.c == "":
            tk.messagebox.showerror(title='警告', message='文本框不能为空')
        elif self.get_student_repetition() == True:
            tk.messagebox.showerror(title='警告', message='学号重复')
        else:
            self.all_student_list.append(self.list1)
            print("添加时的数组：", self.all_student_list)
            for i in self.Tree.get_children():
                self.Tree.delete(i)
            for index in range(len(self.all_student_list)):
                self.Tree.insert("", index, values=(self.all_student_list[index][0], self.all_student_list[index][1],
                                                    self.all_student_list[index][2], self.all_student_list[index][3]))
            self.load_upload_student_files()
            del self.all_student_list
            self.all_student_list = []
            self.load_file_student_info()
            self.load_empty_text()

    # 删除学生信息
    def get_del_student(self):
        try:
            for item in self.Tree.selection():
                item_text = self.Tree.item(item, "values")
            # 数据删除
            # print("列表长度",len(self.all_student_list))
            # print("删学号：",item_text[0])
            for i in range(len(self.all_student_list)):
                # print("第",i,"次")
                # print(self.all_student_list[i][0])
                if self.all_student_list[i][0] == item_text[0]:
                    # print("执行删除")
                    # print("列表1,0是:",self.all_student_list[i][0])
                    # print("删除的列表是",self.all_student_list[i])
                    self.all_student_list.remove(self.all_student_list[i])
                    break
            print("删除后的准备上传数组是:",self.all_student_list)
            # 重载数据
            self.load_upload_student_files()
            # 树状列表中删除选中
            for i in self.all_student_list:
                if i[0] == item_text[0]:
                    self.all_student_list.remove(i)

            print("删除后的树状列表内数组：",self.all_student_list)
            self.Tree.delete(self.Tree.selection())
        except:
            tk.messagebox.showerror(title='系统提示', message='请选中要修改的信息后再修改')

    # 修改学生信息
    def get_amend_studnet(self):
        self.sno = self.Entry_sno.get()
        self.name = self.Entry_name.get()
        score = Score(self.Entry_python.get())  # 重置函数
        score.setScore()
        self.python = str(score.getScore())
        score = Score(self.Entry_c.get())   # 重置函数
        score.setScore()
        self.c = str(score.getScore())
        self.list1 = [self.sno, self.name, self.python, self.c]
        if self.sno == "" or self.name == "" or self.python == "" or self.c == "":
            tk.messagebox.showerror(title='系统提示', message='文本框不能为空')
        else:
            self.get_del_student()
            self.get_add_student()

    # 将数据上传到txt
    def load_upload_student_files(self):
        if not os.path.exists(self.file_path):
            tk.messagebox.showerror(title='警告', message='上传的文件不存在！')
        else:
            # 定义一个临时存储数据的对象
            shuju = ""
            try:
                for i in range(len(self.all_student_list)):
                    for j in range(4):
                        if j == 0:
                            shuju = shuju + self.all_student_list[i][j]
                        elif j == 3 and str(self.all_student_list[i][j]).find("\n") == -1:
                            shuju = shuju + "," + self.all_student_list[i][j] + "\n"
                        else:
                            shuju = shuju + "," + self.all_student_list[i][j]
                print("上传的总数据：\n", shuju)
                with open(file=self.file_path, mode="wb") as fd:
                    fd.write(shuju.encode())
            except:
                tk.messagebox.showerror(title='警告', message='数据上传异常')

    # 清空统计的值
    def load_Empty_values(self):
        self.fail_python = 0            # 不及格
        self.pass_python = 0            # 及格
        self.middle_python = 0          # 中
        self.good_python = 0            # 良
        self.excellent_python = 0       # 优
        self.number_python = 0          # 人数
        self.max_python = 0             # 最大
        self.min_python = 0             # 最小
        self.count_python = 0           # 总成绩
        self.fail_c = 0            # 不及格
        self.pass_c = 0            # 及格
        self.middle_c = 0          # 中
        self.good_c = 0            # 良
        self.excellent_c = 0       # 优
        self.number_c = 0          # 人数
        self.max_c = 0             # 最大
        self.min_c = 0             # 最小
        self.count_c = 0  # 总成绩

    # 统计学生信息
    def get_Statistics_student(self):
        self.load_Empty_values()
        for i in range(len(self.all_student_list)):
            cj_python = int(self.all_student_list[i][2])
            self.count_python = self.count_python + cj_python
            if i == 0:
                self.min_python = cj_python
                self.max_python = cj_python
            if self.min_python > cj_python:
                self.min_python = cj_python
            elif self.max_python < cj_python:
                self.max_python = cj_python
            if cj_python < 60:
                self.fail_python = self.fail_python + 1
                self.number_python = self.number_python + 1
            elif 60 <= cj_python < 70:
                self.pass_python = self.pass_python + 1
                self.number_python = self.number_python + 1
            elif 70 <= cj_python < 80:
                self.middle_python = self.middle_python + 1
                self.number_python = self.number_python + 1
            elif 80 <= cj_python < 90:
                self.good_python = self.good_python + 1
                self.number_python = self.number_python + 1
            elif 90 <= cj_python < 101:
                self.excellent_python = self.excellent_python + 1
                self.number_python = self.number_python + 1
            else:
                print("成绩显示出现错误")
            cj_c = int(self.all_student_list[i][3])
            self.count_c =  self.count_c + cj_python
            if i == 0:
                self.min_c = cj_c
                self.max_c = cj_c
            if self.min_c > cj_c:
                self.min_c = cj_c
            elif self.max_c < cj_c:
                self.max_c = cj_c
            if 0 <= cj_c < 60:
                self.fail_c = self.fail_c + 1
                self.number_c = self.number_c + 1
            elif 60 <= cj_c < 70:
                self.pass_c = self.pass_c + 1
                self.number_c = self.number_c + 1
            elif 70 <= cj_c < 80:
                self.middle_c = self.middle_c + 1
                self.number_c = self.number_c + 1
            elif 80 <= cj_c < 90:
                self.good_c = self.good_c + 1
                self.number_c = self.number_c + 1
            elif 90 <= cj_c < 101:
                self.excellent_c = self.excellent_c + 1
                self.number_c = self.number_c + 1
            else:
                print("成绩显示出现错误")
        print("python的最大值：", self.max_python)
        print("python的最小值：", self.min_python)
        print("python总成绩:", self.count_python)
        print("c的最大值：", self.max_c)
        print("c的最小值：", self.min_c)
        print("c总成绩:", self.count_c)
        print("python不及格：", self.fail_python)
        print("python及格：", self.pass_python)
        print("python中：", self.middle_python)
        print("python良：", self.good_python)
        print("python优：", self.excellent_python)
        print("python人数：", self.number_python)
        print("c不及格：", self.fail_c)
        print("c及格：", self.pass_c)
        print("c中：", self.middle_c)
        print("c良：", self.good_c)
        print("c优：", self.excellent_c)
        print("c人数：", self.number_c)
        # 添加TreeView控件
        self.Tree_statistics = Treeview(self.Pane_right, columns=("course", "max", "min", "average", "fail", "pass", "middle", "good", "excellent", "number"), show="headings", height=20)
        # 设置每一个列的宽度和对齐的方式
        self.Tree_statistics.column("course", width=71, anchor="center")
        self.Tree_statistics.column("max", width=65, anchor="center")
        self.Tree_statistics.column("min", width=65, anchor="center")
        self.Tree_statistics.column("average", width=65, anchor="center")
        self.Tree_statistics.column("fail", width=65, anchor="center")
        self.Tree_statistics.column("pass", width=65, anchor="center")
        self.Tree_statistics.column("middle", width=65, anchor="center")
        self.Tree_statistics.column("good", width=65, anchor="center")
        self.Tree_statistics.column("excellent", width=65, anchor="center")
        self.Tree_statistics.column("number", width=65, anchor="center")
        # 设置每个列的标题
        self.Tree_statistics.heading("course", text="课程")
        self.Tree_statistics.heading("max", text="最高分")
        self.Tree_statistics.heading("min", text="最低分")
        self.Tree_statistics.heading("average", text="平均分")
        self.Tree_statistics.heading("fail", text="不及格")
        self.Tree_statistics.heading("pass", text="及格")
        self.Tree_statistics.heading("middle", text="中")
        self.Tree_statistics.heading("good", text="良")
        self.Tree_statistics.heading("excellent", text="优")
        self.Tree_statistics.heading("number", text="总人数")
        self.Tree_statistics.place(x=10, y=80)
        average_python = self.count_python / self.number_python
        average_c = self.count_c / self.number_c
        self.Tree_statistics.insert("", 0, values=("Python", self.max_python, self.min_python, average_python,
                                        self.fail_python, self.pass_python, self.middle_python,
                                        self.good_python, self.excellent_python, self.number_python))
        self.Tree_statistics.insert("", 1, values=("C语言", self.max_c, self.min_c, average_c,
                                        self.fail_c, self.pass_c, self.middle_c,
                                        self.good_c, self.excellent_c, self.number_c))
        self.Tree.place_forget()

    # 清空文本
    def load_empty_text(self):
        self.Entry_sno.delete(0, "end")
        self.Entry_name.delete(0, "end")
        self.Entry_python.delete(0, "end")
        self.Entry_c.delete(0, "end")

    # 判断学号是否重复
    def get_student_repetition(self):
        self.sno = self.Entry_sno.get()
        for i in range(len(self.all_student_list)):
            if self.all_student_list[i][0] == self.sno:
                return True
                break


if __name__ == '__main__':
    this_main = MainWindow()
    this_main.mainloop()

# str通过encode()方法可以转换为bytes。反过来，bytes通过decode()方法可转换为str