import threading
import socket
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton


class Room:
    def __init__(self):
        self.clients = []

    def addClient(self, c):
        self.clients.append(c)

    def delClient(self, c):
        self.clients.remove(c)

    def sendAllClients(self, msg):
        for c in self.clients:
            c.sendMsg(msg)


class ChatClient(QObject):
    messageReceived = pyqtSignal(str)

    def __init__(self, id, soc, r):
        super().__init__()
        self.id = id
        self.soc = soc
        self.room = r

    @pyqtSlot()
    def recvMsg(self):
        while True:
            data = self.soc.recv(1024)
            msg = data.decode()
            if msg == '/stop':
                self.sendMsg(msg)
                print(self.id, '님 퇴장')
                break

            msg = self.id + ': ' + msg
            self.messageReceived.emit(msg)
            self.room.sendAllClients(msg)

        self.room.delClient(self)
        self.room.sendAllClients(self.id + '님이 퇴장하셨습니다.')

    def sendMsg(self, msg):
        self.soc.sendall(msg.encode(encoding='utf-8'))

    def run(self):
        t = threading.Thread(target=self.recvMsg, args=())
        t.start()


class ServerMain(QObject):
    clientConnected = pyqtSignal(str)
    messageReceived = pyqtSignal(str)

    ip = 'localhost'
    port = 4444

    def __init__(self):
        super().__init__()
        self.room = Room()
        self.server_soc = None

    def open(self):
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_soc.bind((ServerMain.ip, ServerMain.port))
        self.server_soc.listen()

    def run(self):
        self.open()
        print('채팅 서버 시작')
        while True:
            c_soc, addr = self.server_soc.accept()
            self.clientConnected.emit(str(addr))
            msg = '사용할 id:'
            c_soc.sendall(msg.encode(encoding='utf-8'))
            msg = c_soc.recv(1024)
            id = msg.decode()
            cc = ChatClient(id, c_soc, self.room)
            self.room.addClient(cc)
            cc.run()
            print('클라이언트', id, '채팅 시작')


class Client(QObject):
    messageReceived = pyqtSignal(str)

    ip = 'localhost'
    port = 4444

    def __init__(self):
        super().__init__()
        self.client_soc = None

    def conn(self):
        self.client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_soc.connect((Client.ip, Client.port))

    def sendMsg(self, msg):
        self.client_soc.sendall(msg.encode(encoding='utf-8'))

    def recvMsg(self):
        while True:
            data = self.client_soc.recv(1024)
            msg = data.decode()
            self.messageReceived.emit(msg)
            if msg == '/stop':
                break
        self.client_soc.close()

    def run(self):
        self.conn()
        t = threading.Thread(target=self.recvMsg, args=())
        t.start()


class ChatWindow(QWidget):
    def __init__(self, is_server=True):
        super().__init__()
        self.setWindowTitle("Chat Window")
        self.layout = QVBoxLayout()
        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)
        self.input_line = QLineEdit()
        self.layout.addWidget(self.input_line)
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.sendButtonClicked)
        self.layout.addWidget(self.send_button)
        self.setLayout(self.layout)

        self.is_server = is_server
        self.server = None
        self.client = None

        self.messageReceived = pyqtSignal(str)
        self.messageReceived.connect(self.updateChat)

        if self.is_server:
            self.server = ServerMain()
            self.server.clientConnected.connect(self.clientConnected)
            self.server.messageReceived.connect(self.messageReceived)
            self.server.run()
        else:
            self.client = Client()
            self.client.messageReceived.connect(self.messageReceived)
            self.client.run()

    @pyqtSlot(str)
    def updateChat(self, message):
        self.text_edit.append(message)

    def sendButtonClicked(self):
        message = self.input_line.text()
        if self.is_server:
            self.server.room.sendAllClients(message)
        else:
            self.client.sendMsg(message)
        self.input_line.clear()

    @pyqtSlot(str)
    def clientConnected(self, address):
        self.text_edit.append(f"클라이언트가 연결되었습니다. 주소: {address}")


if __name__ == '__main__':
    app = QApplication([])
    server_window = ChatWindow(is_server=True)
    server_window.show()
    client_window = ChatWindow(is_server=False)
    client_window.show()
    app.exec_()
