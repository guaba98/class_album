# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# from UI.UI_mainwidget import Ui_MainWindow
# import client
# import sys

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
port = 1121


class CWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # TODO 클라이언트 PY 파일 생성하고 확인해야 함
        self.c = client.ClientSocket(self)  # 클라이언트 소켓 생성

        self.ip = None
        self.port = None

        self.initUI()

    def __del__(self):
        self.c.stop()

    def initUI(self):
        '''
        컴퓨터 ip : 192.168.56.1
        컴퓨터 자리 고정 ip : 10.10.20.103
        노트북 ip: 192.168.56.1
        '''

        self.ip = '192.168.56.1'  # 임시지정
        self.port = port
        self.connectClicked()

        # 전송하기
        self.chat_send_btn.clicked.connect(self.sendMsg)

    def connectClicked(self):
        if self.c.bConnect == False:
            ip = self.ip
            port = self.port
            if self.c.connectServer(ip, int(port)):
                print('접속 종료')
            else:
                self.c.stop()
                self.chat_lineedit.clear()
                print('접속')
        else:
            self.c.stop()
            self.chat_lineedit.clear()
            print('접속')

    # TODO 메세지 추가해야 함 (클래스 화)
    def updateMsg(self, msg):
        # 여기에 메세지 추가하는 부분 넣기(클래스화)
        print(msg)

    def updateDisconnect(self):
        print('접속')

    def sendMsg(self):
        sendmsg = self.chat_lineedit.text()
        self.c.send(sendmsg)
        self.chat_lineedit.clear()

    def clearMsg(self):
        self.chat_lineedit.clear()

    def closeEvent(self, e):
        self.c.stop()


