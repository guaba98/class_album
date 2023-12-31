from threading import *
from socket import *
from PyQt5.QtCore import Qt, pyqtSignal, QObject


class Signal(QObject): # 소켓 클래스가 연결 끊김, 데이터 수신 시그널 발생 시 window.py 파일이 생성하는 윈도우 창으로 사용자 정의 시그널 보내기 위함
    recv_signal = pyqtSignal(str)
    disconn_signal = pyqtSignal()


class ClientSocket:

    def __init__(self, parent):
        self.parent = parent # 부모 윈도우 저장할 변수 저장 - 데이터 수신, 연결 끊김시 사용할 시그널을 선언하고 부모 윈도으의 슬롯(함수)와 연결

        self.recv = Signal()
        self.recv.recv_signal.connect(self.parent.updateMsg)
        self.disconn = Signal()
        self.disconn.disconn_signal.connect(self.parent.updateDisconnect)

        self.bConnect = False

    def __del__(self): # 라인 소멸자 함수. 부모 윈도우 창에 연결 끊김을 알리는 신호를 보내도록 함.
        self.stop()

    def connectServer(self, ip, port): #부모 윈도우 창에서 '접속'버튼을 눌렀을 때 호출되는 함수. 소켓을 생성하고 해당 ip 주소의 포트번호로 연결 시도
        self.client = socket(AF_INET, SOCK_STREAM)

        try:
            self.client.connect((ip, port))
        except Exception as e: # 접속 시도 후 오류가 있다면 except 구문에서 처리
            print('Connect Error : ', e)
            return False
        else: # 정상적으로 연결이 된다면
            self.bConnect = True # 연결 상태 True
            self.t = Thread(target=self.receive, args=(self.client,)) # 쓰레드 생성, 소켓의 데이터 수신 준비
            self.t.start()
            print('Connected')

        return True

    def stop(self): # 소켓을 닫고, 부모에게 알림
        self.bConnect = False
        if hasattr(self, 'client'):
            self.client.close()
            del (self.client)
            print('Client Stop')
            self.disconn.disconn_signal.emit() #부모에게 알리는 역할

    # 클라이언트 소켓 연결이 정상적으로 이루어지면 생성되는 [쓰레드]에 의해 호출되는 함수.
    # 무한루프를 통해 소켓의 데이터 수신 대기. 소켓의 recv()함수는 호출시 데이터를 수신하기 전까지 블록되어, 다음 코드는 수행하지 않는다.
    def receive(self, client):
        while self.bConnect:
            try:
                recv = client.recv(1024)
            except Exception as e:
                print('Recv() Error :', e)
                break
            else:
                msg = str(recv, encoding='utf-8')
                # 문자열로 인토딩하고 부모 윈도우로 보내 화면에 출력하게 함
                # -> 반드시 쓰레드로 구성되어야 하며, 또 언제 데이터르가 수신될 지 모르므로 무한루프로 구성해 계속 대기해야 한다.
                if msg:
                    self.recv.recv_signal.emit(msg)
                    print('[받은 메세지]:', msg)

        self.stop()

    def send(self, msg): # 부모 윈도으의 '보내기'를 누르면 호출되는 함수.
        if not self.bConnect:
            return

        try:
            self.client.send(msg.encode())
        except Exception as e:
            print('Send() Error : ', e)

