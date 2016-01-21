# -*- encoding: utf8 -*-

__author__ = 'masterpy'

from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *
import os


filename = ''       # 全局文件名变量


def author():
    showinfo('作者信息', '该桌面程序由masterpy编写')


def about():
    showinfo('版权信息.Copyright','本软件版权归属编程，编程，再编程')


# 打开文件，将编辑区的文本清空，然后将打开的文件的内容写入编辑区

def openfile():
    global filename
    filename = askopenfilename(defaultextension='.txt')
    if filename == '':
        filename = None
    else:
        root.title('FileName:'+os.path.basename(filename))
        textPad.delete(1.0, END)     # 1.0代表的是第一行的第一列，END代表的是文本的结尾处
        f = open(filename, 'r')
        textPad.insert(1.0, f.read())
        f.close()


def new():
    global filename
    root.title('未命名文件')     # 新建文件，默认名为未命名
    filename = None
    textPad.delete(1.0,END)     # 将编辑区清空


def save():
    global filename
    try:
        f = open(filename, 'w')
        msg = textPad.get(1.0, END)
        f.write(msg)
        f.close()
    except:
        saveas()


def saveas():
    f = asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')
    global filename
    filename = f
    fh = open(f,'w')
    msg = textPad.get(1.0,END)
    fh.write(msg)
    fh.close()
    root.title('FileName:'+os.path.basename(f))

# 调用tkinter PAI编写剪切、复制、黏贴、重做、撤销函数


def cut():
    textPad.event_generate('<<Cut>>')


def copy():
    textPad.event_generate('<<Copy>>')


def paste():
    textPad.event_generate('<<Paste>>')


def redo():
    textPad.event_generate('<<Redo>>')


def undo():
    textPad.event_generate('<<Undo>>')


def selectAll():
    textPad.tag_add('sel', '1.0', END)


def search():
    topsearch = Toplevel(root)      # 创建搜索窗口
    topsearch.geometry('300x30+200+250')
    label1 = Label(topsearch, text='Find')   # FIND标签
    label1.grid(row=0, column=0, padx=5)     # 标签定位
    entry1 = Entry(topsearch, width=20)      # 输入框
    entry1.grid(row=0, column=1,padx=5)
    button1 = Button(topsearch,text='查找')   # 查找按钮
    button1.grid(row=0, column=2)


root = Tk()
root.title('tkinter nodepad')
root.geometry("800x500+100+100")

# 创建菜单


menubar = Menu(root)
root.config(menu=menubar)

# 文件菜单
filemenu = Menu(menubar)
filemenu.add_command(label='新建', accelerator='Ctrl + N', command=new)
filemenu.add_command(label='打开', accelerator='Ctrl + O', command=openfile)
filemenu.add_command(label='保存', accelerator='Ctrl + S', command=save)
filemenu.add_command(label='另存为', accelerator='Ctrl + Shift + S', command=saveas)
menubar.add_cascade(label='文件', menu=filemenu)


# 编辑菜单
editmenu = Menu(menubar)
editmenu.add_command(label='撤销', accelerator='Ctrl + Z', command=undo)
editmenu.add_command(label='重做', accelerator='Ctrl + y', command=redo)
editmenu.add_separator()
editmenu.add_command(label="剪切", accelerator="Ctrl + X", command=cut)
editmenu.add_command(label="复制", accelerator="Ctrl + C", command=copy)
editmenu.add_command(label="粘贴", accelerator="Ctrl + V", command=paste)
editmenu.add_separator()
editmenu.add_command(label="查找", accelerator = "Ctrl + F", command=search)
editmenu.add_command(label="全选", accelerator = "Ctrl + A", command= selectAll)
menubar.add_cascade(label="编辑", menu=editmenu)

# 关于菜单
aboutmenu = Menu(menubar)
aboutmenu.add_command(label="作者", command=author)
aboutmenu.add_command(label="版权", command = about)
menubar.add_cascade(label="关于", menu=aboutmenu)

# toolbar
toolbar = Frame(root, height=25,bg='light sea green')
shortButton = Button(toolbar, text='打开',command=openfile)
shortButton.pack(side=LEFT, padx=5, pady=5)

shortButton = Button(toolbar, text='保存', command = save)
shortButton.pack(side=LEFT)
toolbar.pack(expand=NO,fill=X)

# Status Bar
status = Label(root, text='Ln20',bd=1, relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM, fill=X)

# linenumber&text

lnlabel =Label(root, width=2, bg='antique white')
lnlabel.pack(side=LEFT, fill=Y)

textPad = Text(root, undo=True)
textPad.pack(expand=YES, fill=BOTH)

scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set) # Y轴滚动条
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)


root.mainloop()

