# -*- coding: utf-8 -*-
from tkinter import  *
import  tkinter.messagebox as a
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        # 创造一个窗口
        self.createWidgets()

    def createWidgets(self):
        # 输入框
        self.helloLabel = Entry(self)
        self.helloLabel.pack()
        # button 并添加button的相应点击事件
        self.quitButton = Button(self, text='Quit', command=self.hello)
        self.quitButton.pack()

    def hello(self):
        # 获取输入框输入内容
        name = self.helloLabel.get() or 'a'
        # 弹出框
        a.showinfo('Message', 'Hello, %s' % name)


app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
