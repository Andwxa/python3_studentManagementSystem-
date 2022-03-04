# coding=utf-8 -*w*- -*x*- -*a*-
from tkinter import *
from tkinter import Entry
from tkinter.ttk import *
import tkinter as tk
import tkinter.messagebox
import os
from tkinter.ttk import Entry
# 教师表
from subject import Subject


class mainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title("课程管理系统")
        self.geometry("900x640+180+80")         # 主窗体大小：900宽 600高 ; 出现位置：180宽 80高
        self.resizable(False, False)            # 不可改变窗体大小
        self["bg"] = "skyblue"                  # 设置主体背景颜色为天蓝色
        # 加载gui
        self.setup_UI()                         # 子容器的加载
        # 开始时的加载数据
        self.all_teacher_list = []
        self.file_path = "course.txt"
        self.load_file_student_info()           # 将数据取出来
        self.load_treeview(self.all_teacher_list)   # 放入TreeView中
        # 初始化搜索课程显示  创建列表和可变字符串
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
        Label_title = Label(self.Pane_top, text="课程管理系统", font=("黑体", 42), background="navy", foreground="white")
        Label_title.place(x=85, y=23)
        # 添加左边按钮
        self.Button_show = Button(self.Pane_left, text="显示所有信息", style="TButton", command=self.load_all_teacher)
        self.Button_show.place(x=20, y=20)
        self.Button_update = Button(self.Pane_left, text="修改任课老师", style="TButton", command=self.get_amend_teacher)
        self.Button_update.place(x=20, y=50)
        self.Button_inquire = Button(self.Pane_left, text="查询课程信息", style="TButton", command=self.get_query_result)
        self.Button_inquire.place(x=20, y=80)
        self.Button_student = Button(self.Pane_left, text="学生管理界面", style="TButton", command=self.spik_student)   #
        self.Button_student.place(x=20, y=420)
        self.Button_again = Button(self.Pane_left, text="重新登陆", style="TButton", command=self.spik)
        self.Button_again.place(x=20, y=450)
        self.Button_out = Button(self.Pane_left, text="退出", style="TButton", command=self.usr_sign_quit)
        self.Button_out.place(x=20, y=480)

        # 添加右边上面
        self.LabelFrame_query = LabelFrame(self.Pane_right, text="教师信息查询", width=660, height=70)
        self.LabelFrame_query.place(x=10, y=10)
        # 添加控件
        self.Label_course = Label(self.LabelFrame_query, text="课程：")
        self.Label_course.place(x=5, y=13)
        self.Entry_course = Entry(self.LabelFrame_query, width=15)      # 查找学号 , textvariable=self.var_course
        self.Entry_course.place(x=50, y=10)

        self.Label_teacher = Label(self.LabelFrame_query, text="任课老师：")
        self.Label_teacher.place(x=175, y=13)
        self.Entry_teacher = Entry(self.LabelFrame_query, width=13)
        self.Entry_teacher.place(x=235, y=10)

        # 添加右下控件
        # 添加TreeView控件
        self.Tree = Treeview(self.Pane_right, columns=("course", "teacher"),show="headings", height=20)
        # 设置每一个列的宽度和对齐的方式
        self.Tree.column("course", width=328, anchor="center")
        self.Tree.column("teacher", width=328, anchor="center")
        # 设置每个列的标题
        self.Tree.heading("course", text="课程")
        self.Tree.heading("teacher", text="任课老师")
        self.Tree.place(x=10, y=80)

    # 退出的函数
    def usr_sign_quit(self):
        self.destroy()

    # 跳转回登录界面
    def spik(self):
        # 关闭当前页面
        self.usr_sign_quit()
        os.system("python login.py")

    # 跳转到教师管理界面
    def spik_student(self):
        # 关闭当前页面
        self.usr_sign_quit()
        # 加载新窗体
        if __name__ == '__main__':
            os.system("python maingui.py")

    # 读取存入数组
    def load_file_student_info(self):
        if not os.path.exists(self.file_path):
            with open(file=self.file_path, mode="wb") as fd:
                sc = 'python,童冰\nC,王长荣'
                fd.write(sc.encode())
            with open(file=self.file_path, mode="rb") as fd:
                # 一次读一行
                current_line = fd.readline()
                while current_line:
                    current_line = current_line.decode()    # 二进制转为str
                    temp_list = current_line.split(",")
                    self.all_teacher_list.append(temp_list)
                    # 读取下一行,读完了循环就结束了
                    current_line = fd.readline()
                print("文件读取出来的:", self.all_teacher_list)
        else:
            try:
                with open(file=self.file_path, mode="rb") as fd:
                    # 一次读一行
                    current_line = fd.readline()
                    while current_line:
                        current_line = current_line.decode()  # 二进制转为str
                        temp_list = current_line.split(",")
                        self.all_teacher_list.append(temp_list)
                        # 读取下一行,读完了循环就结束了
                        current_line = fd.readline()
                    print("文件里读取出来的:",self.all_teacher_list)
            except:
                tk.messagebox.showerror(title='警告', message='课程数据读取异常')

    # 将数组放入到TreeView中
    def load_treeview(self, current_list: list):
        # 判断是否有数据：
        if len(current_list) == 0:
            tk.messagebox.showerror(title='系统消息', message='没有数据加载')
        else:
            for index in range(len(current_list)):
                self.Tree.insert("", index, values=(current_list[index][0], current_list[index][1]))

    # 按照课程进行查询
    def get_query_result(self):
        self.course = self.Entry_course
        if self.course == "":
            tk.messagebox.showerror(title='警告', message='文本框不能为空')
        else:
            # TreeView中的内容清空
            for i in self.Tree.get_children():
                self.Tree.delete(i)
            # 准备查询条件：获取课程
            query_condition = self.Entry_course.get()
            # 遍历List获取符合条件的教师信息
            for item in self.all_teacher_list:
                if query_condition in item[0]:
                    # 满足条件的课程
                    self.query_result_list.append(item)
            # 把结果加载的TreeView中
            self.load_treeview(self.query_result_list)
            # 将列表结果清除
            self.query_result_list.clear()

    # 显示所有信息
    def load_all_teacher(self):
        try:
            self.Tree.place(x=10, y=80)
            self.Tree_statistics.place_forget()
            # TreeView中的内容清空
            for i in self.Tree.get_children():
                self.Tree.delete(i)
            # 加载所有的教师信息到treeview
            self.load_treeview(self.all_teacher_list)
        except:
            # TreeView中的内容清空
            for i in self.Tree.get_children():
                self.Tree.delete(i)
            # 加载所有的教师信息到treeview
            self.load_treeview(self.all_teacher_list)

    # 修改教师信息
    def get_amend_teacher(self):
        xuanz = 0
        self.teacher = self.Entry_teacher.get()
        for item in self.Tree.selection():
            item_text = self.Tree.item(item, "values")
        for i in range(len(self.all_teacher_list)):
            xuanz = i
            if self.all_teacher_list[i][0] == item_text[0]:
                self.all_teacher_list[i][1] = self.teacher
                break
        print("修改后的准备上传数组是:", self.all_teacher_list)
        # 重载数据
        self.load_upload_teacher_files()
        # 树状列表中修改选中
        for i in self.all_teacher_list:
            if i[0] == item_text[0]:
                self.all_teacher_list[xuanz][1] = self.teacher
        # print("删除后的树状列表内数组：", self.all_teacher_list)
        # self.Tree.delete(self.Tree.selection())
        for i in self.Tree.get_children():
            self.Tree.delete(i)
        # 加载所有的教师信息到treeview
        self.load_treeview(self.all_teacher_list)

    # 将数据上传到txt
    def load_upload_teacher_files(self):
        if not os.path.exists(self.file_path):
            tk.messagebox.showerror(title='警告', message='上传的文件不存在！')
        else:
            # 定义一个临时存储数据的对象
            shuju = ""
            try:
                for i in range(len(self.all_teacher_list)):
                    for j in range(2):
                        if j == 0:
                            shuju = shuju + self.all_teacher_list[i][j]
                        elif j == 1 and str(self.all_teacher_list[i][j]).find("\n") == -1:
                            shuju = shuju + "," + self.all_teacher_list[i][j] + "\n"
                        else:
                            shuju = shuju + "," + self.all_teacher_list[i][j]
                print("上传的总数据：\n", shuju)
                with open(file=self.file_path, mode="wb") as fd:
                    fd.write(shuju.encode())
            except:
                tk.messagebox.showerror(title='警告', message='数据上传异常')

    # 清空文本
    def load_empty_text(self):
        self.Entry_course.delete(0,"end")
        self.Entry_teacher.delete(0,"end")


if __name__ == '__main__':
    this_main = mainWindow()
    this_main.mainloop()

# str通过encode()方法可以转换为bytes。反过来，bytes通过decode()方法可转换为str