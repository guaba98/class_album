from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import socket
import server
from UI.UI_server import Ui_server_form

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

port = 1121


class CWidget(QWidget, Ui_server_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.s = server.ServerSocket(self)
        self.initUI()

    def initUI(self):

        # 아이피
        host_ip = socket.gethostbyname(socket.gethostname())  # 현재 호스트 주소 자동 알려줌
        self.host_ip_lineedit.setText(str(host_ip))  # ip 번호 입력
        # self.ip = self.host_ip_lineedit.text() # 최종 아이피는 유저가 입력한 ip

        # 포트번호
        self.host_port_lineedit.setText(str(port))
        # self.port = self.host_ip_lineedit.text()

        # 버튼 선택시 연결 이벤트 생성
        self.server_start_btn.toggled.connect(self.toggleButton)

        # 접속자 정보 부분
        self.tableWidget_members.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 열 자동정렬

        # 채팅창 부분
        # TODO sendMsg 함수 연결 필요
        self.send_btn.clicked.connect(self.sendMsg)

    def toggleButton(self, state):
        """상태에 따라 값 바꿔주기"""
        if state:
            ip = self.host_ip_lineedit.text()
            port = self.host_port_lineedit.text()
            if self.s.start(ip, int(port)):
                self.server_start_btn.setText('서버 종료')
        else:
            self.s.stop()
            self.chat_listwidget.clear()
            self.server_start_btn.setText('서버 실행')

    def updateClient(self, addr, isConnect=False):
        print('주소번호',addr)
        row = self.tableWidget_members.rowCount()
        if isConnect:
            self.tableWidget_members.setRowCount(row + 1)
            self.tableWidget_members.setItem(row, 0, QTableWidgetItem(addr[0]))
            self.tableWidget_members.setItem(row, 1, QTableWidgetItem(str(addr[1])))
        else:
            for r in range(row):
                ip = self.tableWidget_members.item(r, 0).text()  # ip
                port = self.tableWidget_members.item(r, 1).text()  # port
                if addr[0] == ip and str(addr[1]) == port:
                    self.tableWidget_members.removeRow(r)
                    break

    def updateMsg(self, name, msg):
        print('[server_window.py]클라이언트에서 받은 메세지: ', name, msg)
        if msg.startswith('LOGIN_REQ'):
            msg_ = msg.replace('LOGIN_REQ', '')
            email = msg_.split(':')[0]
            self.chat_listwidget.addItem(QListWidgetItem(f'{email}님 로그인 시도'))
        else:
            self.chat_listwidget.addItem(QListWidgetItem(name+msg))
            self.chat_listwidget.setCurrentRow(self.chat_listwidget.count() - 1)

    # def handle_login_request(self, id, pw):
    #     print('[server_window.py]클라이언트가 전송한 아이디, 비밀법호', id, pw)
    #     self.s.
    #     pass

    def sendMsg(self):
        if not self.s.bListen:
            self.chat_lineedit.clear()  # 라인에딧 창 클리어
            return
        sendmsg = '[공지]' + self.chat_lineedit.text()
        self.updateMsg(sendmsg)
        print('[서버] 보낸 메세지: ',sendmsg)
        self.s.send(sendmsg)
        self.chat_lineedit.clear()

    def clearMsg(self):
        self.chat_lineedit.clear()  # 사용할 일 있으면

    def closeEvent(self, e) -> None:
        self.s.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    w.show()
    sys.exit(app.exec_())
