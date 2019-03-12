#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on Tue Mar 12 15:53:52 2019
本demo程序利用纵向分布将LCD模块与Slider模块进行组合
通过滑动Slider改变LCD的数字显示
@author: wzy
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication


class SigSlot(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.setWindowTitle('Timer')
        lcd = QLCDNumber(self)
        # 滑动条
        slider = QSlider(Qt.Horizontal, self)
        # 纵向分布
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)
        self.setLayout(vbox)
        # 滑动条改变LCD的数字显示
        slider.valueChanged.connect(lcd.display)
        self.resize(350, 250)


app = QApplication(sys.argv)
qb = SigSlot()
qb.show()
sys.exit(app.exec_())
