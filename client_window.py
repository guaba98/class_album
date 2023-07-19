from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from UI.UI_mainwidget import Ui_MainWindow
import sys
import client

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
port = 1121

class CWidget(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # TODO 클라이언트 PY 파일 생성하고 확인해야 함
        self.c = client.ClientSocket(self) # 클라이언트 소켓 생성

        self.initUI()

    def __del__(self):
        self.c.stop()

    def initUI(self):
        '''
        컴퓨터 ip : 192.168.56.1
        컴퓨터 자리 고정 ip : 10.10.20.103
        노트북 ip:
        '''


        self.ip = '192.168.56.1' # 임시지정
        self.port = port


