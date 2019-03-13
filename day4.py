#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on Wed Mar 13 09:33:23 2019
利用表盘控件改变LCD的显示数值
@author: wzy
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QDial, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)
        # 设置刻度可见
        dial.setNotchesVisible(True)
        # 设置大刻度
        dial.setPageStep(20)
        # 设置小刻度
        dial.setNotchTarget(10)
        # 设置范围
        dial.setMinimum(0)
        dial.setMaximum(1999)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Signal and Slot')
        lcd.setGeometry(100, 50, 150, 60)
        dial.setGeometry(120, 120, 100, 100)
        dial.valueChanged.connect(lcd.display)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
