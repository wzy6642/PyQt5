# -*- coding: utf-8 -*-
# @Time    : 2021/8/11 9:12
# @Author  : Zhenyu Wu
# @Email   : wuzhenyuai@gmail.com
# @File    : main.py
# @Software: PyCharm
# 顺序：
#           1、Tools -> External Tools -> QtDesigner（绘制界面） -> 保存为`UI文件名.ui`
#           2、右击`UI文件名.ui` -> External Tools -> PyUIC -> 生成`UI文件名.py`
#           3、右击项目文件夹 -> Mark Directory as -> Sources Root
#           4、新建`main.py` -> 添加下述代码并运行
# 界面与逻辑分离
# 后续将日志功能加入
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from Main_Window import Ui_MainWindow                   # 导入主窗口
from Login_Dialog import Ui_Dialog                      # 导入弹窗
from Algorithms import algorithm_name                   # 导入要执行的算法


# 新建类继承于UI类，方便进一步书写逻辑
class Application(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        self.setupUi(self)             # 创建界面
        ## 一些控件的属性初始化代码
        self.window_attribute()

        ## 一些算法实例化代码
        self.algorithm_name = algorithm_name(value_1=None)

        ## 信号和槽函数部分
        self.test_button.clicked.connect(lambda: self.test(
            self.test_button,
        ))

    ## 控件属性定义部分
    def window_attribute(self):
        # 属性的具体定义部分
        self.setWindowTitle("PyQt5主窗口模板")

    ## 自定义槽函数部分
    def test(self, button):
        # 这里编写触发事件对应的执行代码
        print(button.text())
        self.algorithm_name.calculate()


# 新建类继承于对话框类，方便进一步书写逻辑
class Login(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)             # 创建界面
        ## 一些控件的属性初始化代码
        self.dialog_attribute()

        ## 一些算法实例化代码
        self.algorithm_name = algorithm_name(value_1=None)

        ## 信号和槽函数部分
        self.dialog_button.clicked.connect(lambda: self.test(
            self.dialog_button,
        ))

    ## 控件属性定义部分
    def dialog_attribute(self):
        # 属性的具体定义部分
        self.setWindowTitle("登录窗口")

    ## 自定义槽函数部分
    def test(self, button):
        # 这里编写触发事件对应的执行代码
        self.algorithm_name.calculate()
        self.close()


# 设计不同页面之间的逻辑关系
def Interaction_Logic(main_window, login_dialog):
    main_window.test_button.clicked.connect(login_dialog.show)


if __name__ == '__main__':
    app = QApplication(sys.argv)                    # 创建应用程序对象
    mainWindow = Application()                      # 实例化界面
    loginDialog = Login()                           # 实例化对话框窗口
    Interaction_Logic(mainWindow, loginDialog)      # 页面之间的逻辑设计
    mainWindow.show()                               # 窗口显示
    sys.exit(app.exec_())                           # 主循环结束
