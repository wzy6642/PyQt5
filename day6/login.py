#!/usr/bin/env python
# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu
from PyQt5.QtGui import QIcon
import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.statusBar().showMessage('准备就绪')
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('文档')
        self.setWindowIcon(QIcon('python.ico'))
        exitAct = QAction(QIcon('exit.ico'), '退出(&E)', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')
        exitAct.triggered.connect(qApp.quit)
        saveMenu = QMenu('保存方式(&S)', self)
        saveAct = QAction(QIcon('save.ico'), '保存...', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('保存文件')
        saveasAct = QAction(QIcon('save_as.ico'), '另存为...(&O)', self)
        saveasAct.setStatusTip('文件另存为')
        saveMenu.addAction(saveAct)
        saveMenu.addAction(saveasAct)
        newAct = QAction(QIcon('new.ico'), '新建(&N)', self)
        newAct.setShortcut('Ctrl+N')
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件(&F)')
        fileMenu.addAction(newAct)
        fileMenu.addMenu(saveMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)
        toolbar = self.addToolBar('工具栏')
        toolbar.addAction(newAct)
        toolbar.addAction(exitAct)
        self.show()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        newAct = cmenu.addAction('新建')
        opnAct = cmenu.addAction('保存')
        quitAct = cmenu.addAction('退出')
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            qApp = quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
