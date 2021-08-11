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
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Template import Ui_MainWindow                      # 导入UI类


# 新建类继承于UI类，方便进一步书写逻辑
class Application(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)        # 创建应用程序对象
    mainWindow = Application()
    mainWindow.show()                   # 窗口显示
    sys.exit(app.exec_())               # 主循环结束
