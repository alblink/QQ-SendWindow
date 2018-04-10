# -*- coding:utf-8 -*-
"""

@Time    : 2018/4/10 20:48
@Author  : YeJian
@File    : demo.py

"""

from tkinter import *
import time


def main():
    # 发送
    def sendMsg():
        strMsg = '我：'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n'
        txtMsglist.insert(END, strMsg)  # 添加到第一个文本框
        txtMsglist.insert(END, txtMsg.get('0.0', END)+'\n\n')
        txtMsg.delete('0.0', END)

    # 取消
    def cancelMsg():
        txtMsg.delete('0.0', END)



    t = Tk()  # 实例化一个对象
    t.title('与XX聊天中')

    # 创建frame容器
    frmLT = Frame(width=500, height=320, bg='white')
    frmLC = Frame(width=500, height=150, bg='white')
    frmLB = Frame(width=500, height=30, bg='white')
    frmRT = Frame(width=200, height=500)

    # 布局
    frmLT.grid()
    frmLC.grid()
    frmLB.grid()
    frmRT.grid(row=0, column=1, rowspan=3, padx=2, pady=3)  # row行，column列，rowspan合并，padx左右，pady上下

    # 创建控件
    txtMsglist = Text(frmLT)  # 显示多行文本
    txtMsg = Text(frmLC)

    # 控件+图片
    btnSend = Button(frmLB, text='发送', width=8, command=sendMsg)
    btnCancle = Button(frmLB, text='取消', width=8, command=cancelMsg)

    # 添加图片
    imageLink = PhotoImage(file='111.gif')
    lblImage = Label(frmRT, image=imageLink)  # Label可显示文字或图片

    btnSend.grid(row=2, column=1)
    btnCancle.grid(row=2, column=2)
    lblImage.grid()
    txtMsglist.grid()
    txtMsg.grid()

    frmLT.grid_propagate(0)
    frmLC.grid_propagate(0)
    frmLB.grid_propagate(0)
    frmRT.grid_propagate(0)

    t.mainloop()  # 发送命令，进入消息循环中，创建窗口


if __name__ == '__main__':  # 判断文件入口
    main()



