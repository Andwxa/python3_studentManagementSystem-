import pickle
import random
import tkinter as tk
import tkinter.messagebox
from tkinter import *
from maingui import MainWindow


class login_main(object):
    def __init__(self):
        super().__init__()              # 先执行tk这个类的初始化
        # 错误次数
        self.login_worng = 0
        # 验证码值
        self.verification_Code = login_main.verifycode(self)
        # 主窗口
        self.window = Tk()
        self.window.title('学生管理系统')
        self.window.geometry('450x300')
        self.window["bg"] = "skyblue"  # 设置主体背景颜色为天蓝色
        # 设置登录窗口大小不可拉伸
        self.window.resizable(width=False, height=False)
        # 标签 用户名密码
        tk.Label(self.window, text='学生管理系统', font=("黑体", 32), bg="skyblue").place(x=90, y=20)
        tk.Label(self.window, text='用户名:', bg="skyblue").place(x=110, y=100)
        tk.Label(self.window, text='密   码:', bg="skyblue").place(x=110, y=140)
        tk.Label(self.window, text='验证码:', bg="skyblue").place(x=110, y=180)
        tk.Label(self.window, text=self.verification_Code, background='white').place(x=320, y=180)
        # 用户名输入框
        self.var_usr_name = tk.StringVar()
        self.entry_usr_name = tk.Entry(self.window, textvariable=self.var_usr_name)
        self.entry_usr_name.place(x=170, y=100)
        # 密码输入框
        self.var_usr_pwd = tk.StringVar()
        self.entry_usr_pwd = tk.Entry(self.window, textvariable=self.var_usr_pwd, show='*')
        self.entry_usr_pwd.place(x=170, y=140)
        # 验证码输入框
        self.var_usr_vercode = tk.StringVar()
        self.var_usr_vercode = tk.Entry(self.window, textvariable=self.var_usr_vercode)
        self.var_usr_vercode.place(x=170, y=180)
        print(self.verification_Code)
        # 登录和取消按钮
        self.bt_login = tk.Button(self.window, text='登录', width=8, command=self.usr_log_in)
        self.bt_login.place(x=140, y=230)
        self.bt_logquit = tk.Button(self.window, text='退出', width=8, command=self.usr_sign_quit)
        self.bt_logquit.place(x=240, y=230)

    # 启动函数
    def run(self):
        # 主循环
        self.window.mainloop()

    # 随机验证码
    def verifycode(self):
        # 验证码
        code_list = ''
        # 每一位验证码都有三种可能（大写字母，小写字母，数字）
        for i in range(6):  # 控制验证码生成的位数
            state = random.randint(1, 3)
            if state == 1:
                first_kind = random.randint(65, 90)  # 大写字母
                random_uppercase = chr(first_kind)
                code_list = code_list + random_uppercase
            elif state == 2:
                second_kinds = random.randint(97, 122)  # 小写字母
                random_lowercase = chr(second_kinds)
                code_list = code_list + random_lowercase
            elif state == 3:
                third_kinds = random.randint(0, 9)
                code_list = code_list + str(third_kinds)
        return code_list

    # 登录函数
    def usr_log_in(self):
        # 输入框获取用户名密码
        # 用户名
        usr_name = self.var_usr_name.get()
        # 密码
        usr_pwd = self.var_usr_pwd.get()
        # 验证码
        var_vercode = self.var_usr_vercode.get()
        # 从本地字典获取用户信息，如果没有则新建本地数据库
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                usrs_info = pickle.load(usr_file)
        except FileNotFoundError:
            with open('usr_info.pickle', 'wb') as usr_file:
                usrs_info = {'teacher': 'teacher'}
                pickle.dump(usrs_info, usr_file)
        if self.login_worng < 3:
            # 判断用户名和密码是否匹配
            if usr_name in usrs_info:
                if usr_pwd == usrs_info[usr_name]:
                    if var_vercode == self.verification_Code.lower() or var_vercode == self.verification_Code:
                        tk.messagebox.showinfo(title='登录成功', message='欢迎您：' + usr_name)
                        self.user = usr_name
                        self.login_worng = 0
                        self.spik()
                    else:
                        tk.messagebox.showerror(message='验证码错误')
                else:
                    num = 2 - self.login_worng
                    tk.messagebox.showwarning(title='登录失败', message="密码错误,还有" + str(num) + "次机会")
                    self.login_worng = self.login_worng+1
            # 用户名密码不能为空
            elif usr_name == '' or usr_pwd == '':
                tk.messagebox.showerror(message='用户名或密码为空')
            # w弹出不存x在这个账户的a框
            else:
                tk.messagebox.showwarning(title='登录失败', message='没有这个账户')
        else:
            tk.messagebox.showerror(title='警告', message='输入的密码错误达到最大次数，请联系管理人员')

    # 退出的函数
    def usr_sign_quit(self):
        self.window.destroy()

    # 跳转
    def spik(self):
        # 关闭当前页面
        self.usr_sign_quit()
        # 加载新窗体
        if __name__ == '__main__':
            MainWindow()


if __name__ == '__main__':
    login_main = login_main()
    login_main.run()
