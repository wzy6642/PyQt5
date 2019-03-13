#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on Wed Mar 13 09:33:23 2019
按住上、下、左、右方向键的时候，窗口中依次会出现对应方位。
@author: wzy
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Direction Show')
        self.lab = QLabel('方向', self)
        self.lab.setGeometry(150, 150, 100, 100)
        self.show()

    # 重新实现了keyPressEvent()事件处理程序
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
            self.lab.setText('↑')
        elif e.key() == Qt.Key_Down:
            self.lab.setText('↓')
        elif e.key() == Qt.Key_Left:
            self.lab.setText('←')
        else:
            self.lab.setText('→')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
