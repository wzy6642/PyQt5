# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 15:39
# @Author  : Zhenyu Wu
# @Email   : wuzhenyuai@gmail.com
# @File    : run.py
# @Software: PyCharm
# @Reference: https://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding
#             https://res.abeim.cn/api/weather/doc.php
import sys
import requests
import re
import matplotlib.pyplot as plt
from Weather import Ui_Form
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

my_key = '*******'


class Weather_Info(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Weather_Info, self).__init__(parent)
        self.setupUi(self)
        self.img.setAlignment(Qt.AlignCenter)
        self.loc_scan.clicked.connect(lambda: self.get_lon_lat(
            location_name=self.position.text(),
        ))
        self.loc_scan.clicked.connect(lambda: self.get_weather(
            lng=self.longitude.text(),
            lat=self.latitude.text(),
            state=1,
        ))
        self.temp_radioButton.toggled.connect(lambda: self.get_weather(
            lng=self.longitude.text(),
            lat=self.latitude.text(),
            state=2,
        ))
        self.radioButton.toggled.connect(lambda: self.get_weather(
            lng=self.longitude.text(),
            lat=self.latitude.text(),
            state=3,
        ))

    # 根据地点名称获取其经纬度以及简单的描述信息
    def get_lon_lat(self, location_name):
        location_api = 'https://api.map.baidu.com/geocoding/v3/?address={}&output=json&ak={}&callback=showLocation'.format(
            location_name, my_key)
        try:
            res = requests.get(location_api)
            res = res.text
        except Exception as e:
            print(e)
        res = eval(re.findall('{.*}', res)[0])
        self.longitude.setText(str(round(res['result']['location']['lng'], 6)))
        self.latitude.setText(str(round(res['result']['location']['lat'], 6)))
        self.information.setText(str(res['result']['level']))

    # 根据经纬度获取天气信息
    def get_weather(self, lng, lat, state):
        weather_api = 'https://res.abeim.cn/api-weather?lng={}&lat={}'.format(lng, lat)
        try:
            res = requests.get(weather_api)
            res = res.json()
        except Exception as e:
            print(e)
        if state==1:
            self.temp_location.setText(res['地址'])
            self.time_stamp.setText(res['更新时间'])
            self.temp_now.setText(res['现在']['温度'])
            self.humidity_now.setText(res['现在']['湿度'])
            self.pressure.setText(res['现在']['气压'])
        elif state==2:
            temp = [i['温度'] for i in res['小时预报']['温度']]
            plt.figure()
            plt.plot(list(range(1, len(temp)+1)), temp)
            plt.xlabel('距离现在多少个小时')
            plt.ylabel('温度')
            plt.grid()
            plt.savefig('img/1.jpg')
            self.img.setPixmap(QPixmap('img/1.jpg'))
        elif state==3:
            temp = [float(i['风速']) for i in res['小时预报']['风']]
            plt.figure()
            plt.plot(list(range(1, len(temp)+1)), temp)
            plt.xlabel('距离现在多少个小时')
            plt.ylabel('风速')
            plt.grid()
            plt.savefig('img/2.jpg')
            self.img.setPixmap(QPixmap('img/2.jpg'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Weather_Info()
    mainWindow.show()
    sys.exit(app.exec_())
