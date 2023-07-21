from threading import *
from socket import *
from PyQt5.QtCore import Qt, pyqtSignal, QObject


class Signal(QObject):  # 소켓 클래스가 연결 끊김, 데이터 수신 시그널 발생 시 window.py 파일이 생성하는 윈도우 창으로 사용자 정의 시그널 보내기 위함
    recv_signal = pyqtSignal(str)  # 메세지 받는 시그널
    disconn_signal = pyqtSignal()  # 연결 끊는 시그널
    login_signal = pyqtSignal(str) # 로그인 시그널
    email_signal = pyqtSignal(str) # 이메일 확인 시그널
    register_signal = pyqtSignal(str, str, str, str, str) # 회원가입 시그널(이름, 이메일, 핸드폰번호, 비밀번호, 가입일자)

class ClientSocket:

    def __init__(self, parent):
        self.parent = parent  # 부모 윈도우 저장할 변수 저장 - 데이터 수신, 연결 끊김시 사용할 시그널을 선언하고 부모 윈도으의 슬롯(함수)와 연결
        # 시그널 제작
        self.recv = Signal()
        self.recv.recv_signal.connect(self.parent.updateMsg)
        self.disconn = Signal()
        self.disconn.disconn_signal.connect(self.parent.updateDisconnect)
        self.login = Signal()
        self.login.login_signal.connect(self.parent.receive_login)
        self.email = Signal()
        self.email.email_signal.connect(self.parent.receive_email)


        self.bConnect = False

    def __del__(self):  # 라인 소멸자 함수. 부모 윈도우 창에 연결 끊김을 알리는 신호를 보내도록 함.
        self.stop()

    def connectServer(self, ip, port):  # 부모 윈도우 창에서 '접속'버튼을 눌렀을 때 호출되는 함수. 소켓을 생성하고 해당 ip 주소의 포트번호로 연결 시도
        self.client = socket(AF_INET, SOCK_STREAM)

        try:
            self.client.connect((ip, port))
        except Exception as e:  # 접속 시도 후 오류가 있다면 except 구문에서 처리
            print('[클라이언트] 연결 에러 : ', e)
            return False
        else:  # 정상적으로 연결이 된다면
            self.bConnect = True  # 연결 상태 True
            self.t = Thread(target=self.receive, args=(self.client,))  # 쓰레드 생성, 소켓의 데이터 수신 준비
            self.t.start()
            print('[클라이언트] 연결됨')

        return True

    def stop(self):  # 소켓을 닫고, 부모에게 알림
        self.bConnect = False
        if hasattr(self, 'client'):
            self.client.close()
            del (self.client)
            print('[클라이언트] Stop')
            self.disconn.disconn_signal.emit()  # 부모에게 알리는 역할

    # 클라이언트 소켓 연결이 정상적으로 이루어지면 생성되는 [쓰레드]에 의해 호출되는 함수.
    # 무한루프를 통해 소켓의 데이터 수신 대기. 소켓의 recv()함수는 호출시 데이터를 수신하기 전까지 블록되어, 다음 코드는 수행하지 않는다.
    def receive(self, client):
        signal_dict = {
            'avlbl_email': self.email.email_signal.emit,
            'n_avlbl_email': self.email.email_signal.emit,
            'vaild_id': self.login.login_signal.emit,
            'reject_login': self.login.login_signal.emit,
        }
        # 문자열로 인코딩하고 부모 윈도우로 보내 화면에 출력하게 함
        # -> 반드시 쓰레드로 구성되어야 하며, 또 언제 데이터르가 수신될 지 모르므로 무한루프로 구성해 계속 대기해야 한다.
        while self.bConnect:
            try:
                recv = client.recv(1024)
            except Exception as e:
                print('Recv() Error :', e)
                break
            else:
                msg = str(recv, encoding='utf-8') # 인코딩
                print('[client.py] 수신 타입', type(msg), '받은메세지', msg)

                # 시그널 전달
                if msg in list(signal_dict.keys()):
                    signal_dict[msg](msg)
                    print('[client.py]', msg, '메세지')
                else:
                    self.recv.recv_signal.emit(msg)
                    print('[cilent.py 받은 메세지]:', msg)

        self.stop()

    # 하는중 하는중 하는중 0720
    def login_request(self, username, password):
        self.client.send(('LOGIN_REQ' + username + ":" + password).encode())
        # self.client.login_signal.emit(username, password)  # 로그인 요청 시그널 호출

    def check_vaild_email(self, email):
        self.client.send(('CHECK_EMAIL' + email).encode())
        print('2. 클라이언트에서 이메일을 서버로 보냅니다.', email)

    def register_request(self, username, password, user_num, email, r_date):
        """유저 정보를 받아와서 db에 저장 신호를 보냄"""
        self.client.send(f'SIGNUP_REQ{username}:{password}:{user_num}:{email}:{r_date}'.encode())  # 회원가입 요청 시그널 호출

    def duplicate_check_request(self, username):
        self.client.duplicate_check_signal.emit(username)  # 로그인 중복 체크 요청 시그널 호출

    def send(self, msg):  # 부모 윈도우의 '보내기'를 누르면 호출되는 함수.
        if not self.bConnect:
            return
        try:
            self.client.send(msg.encode())
        except Exception as e:
            print('Send() Error : ', e)

    # def login_req(self, data):
    #     try:
    #         self.client.send(data.en)
