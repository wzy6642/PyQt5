#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on Tue Mar 12 15:53:52 2019
本demo程序给窗口添加图标并且创建一个按钮实现关闭窗口的功能
@author: wzy
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class Ico(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Window with Ico')
        self.setWindowIcon(QIcon('stock.ico'))
        qbtn = QPushButton('退出', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(70, 30)
        qbtn.move(50, 50)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())
