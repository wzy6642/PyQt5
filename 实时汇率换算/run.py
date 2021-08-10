# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 8:41
# @Author  : Zhenyu Wu
# @Email   : wuzhenyuai@gmail.com
# @File    : run.py
# @Software: PyCharm
import sys
import requests
import re
import pprint
import pandas as pd
from Exchange import Ui_Form
from PyQt5.QtWidgets import QMainWindow, QApplication


# 获取国际汇率
def Get_Rate_All():
    rate = [i for i in requests.get('http://hl.anseo.cn/').text.replace('正无穷大', '99999').split('\n') if '人民币' in i and '1 ' in i][1:]
    rate_num = [re.findall('(\d+)(\.\d+)?', i) for i in rate]
    rate_num = [(float(''.join(i[0])), float(''.join(i[1]))) for i in rate_num]
    rate_dis = [re.findall('[\u4E00-\u9FA5]+', i)[:2] for i in rate]
    rate = [[rate_num[i][0], rate_dis[i][0], rate_num[i][1], rate_dis[i][1]] for i in range(len(rate_num))]
    rate = pd.DataFrame({'source_value': [i[0] for i in rate],
                         'source': [i[1] for i in rate],
                         'target_value': [i[2] for i in rate],
                         'target': [i[3] for i in rate],
                         })
    return rate


class Exchange_Rate(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Exchange_Rate, self).__init__(parent)
        self.setupUi(self)
        self.rate_all = Get_Rate_All()
        self.add_item(self.rate_all)
        self.convert_button.clicked.connect(lambda: self.get_item(
            source=self.source.currentText(),
            target=self.target.currentText(),
            source_value=self.source_value.value(),
            rate_all=self.rate_all,
        ))

    # 为下拉框添加元素
    def add_item(self, rate_all):
        # all_items = list(set(list(self.rate_all['source'])+list(self.rate_all['target'])))
        all_items = list(set(list(self.rate_all['source'])))
        for i in range(len(all_items)):
            self.source.addItems(all_items)
            self.target.addItems(all_items)
            # self.source.setItemText(i, all_items[i])
            # self.target.setItemText(i, all_items[i])

    # 获取待转换的币种以及原始币种值
    def get_item(self, source, target, source_value, rate_all):
        if source != '人民币' and target != '人民币':
            rate_1 = list(rate_all[rate_all['source'].isin([source])]['target_value'])[0]
            rate_2 = list(rate_all[rate_all['target'].isin([target])]['target_value'])[0]
            convert = source_value * rate_1 * rate_2
        elif source == target:
            convert = source_value
        elif source == '人民币':
            rate = list(rate_all[rate_all['target'].isin([target])]['target_value'])[0]
            convert = source_value * rate
        elif target == '人民币':
            rate = list(rate_all[rate_all['source'].isin([source])]['target_value'])[0]
            convert = source_value * rate
        # pprint.pprint(convert)
        convert = round(convert, 3)
        self.target_value.setText(str(convert))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Exchange_Rate()
    mainWindow.show()
    sys.exit(app.exec_())
