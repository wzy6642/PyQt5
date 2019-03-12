#!/usr/bin/env python
# -*- coding:utf-8 -*-
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
