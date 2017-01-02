#!/usr/bin/python
#  -*- coding: utf-8 -*-
'''  注释也可以使用 [#coding=utf-8] '''
import sys  
'''这里我们进行必须的引用。基础的GUI控件位于QtGui模块中。'''
from PyQt4 import QtGui  
'''
    能弹出一个方框的界面
'''

'''每一个PyQT4应用必须创建一个应用对象。应用对象位于QtGui模块中。sys.argv参数是从命令行返回的一个参数列表。Python脚本可以从shell来运行。这是一种我们启动脚本的方法。'''
app = QtGui.QApplication(sys.argv)  
'''QWidget控件是PyQT4中所有用户接口对象的基类。我们为QWidget提供了缺省的构造程序。缺省的构造程序没有父类。一个没有父类的控件叫做窗口。'''
widget = QtGui.QWidget()  
'''resize()方法可以调整控件的尺寸。这里是250px宽，150px高。'''
widget.resize(250, 150)  
'''这里我们指定我们窗口的标题。标题在标题栏里显示。'''
widget.setWindowTitle('Love Guige,Love Python')  
'''show() 方法将控件显示在屏幕上。'''
widget.show()  
'''sys.exit()方法可以确保一个干净的退出。环境参数会显示出应用程序是何种方式结束的'''
sys.exit(app.exec_()) 
