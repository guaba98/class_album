import os.path
from threading import Thread  # 파이썬 모듈 불러오기
from socket import *
import base64
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from Source.DataClass import DataClass
from Source.dig_warning import DialogWarning


class ServerSocket(QObject):  # 네트워크 관련 클래스
    update_signal = pyqtSignal(tuple, bool)
    recv_signal = pyqtSignal(str, str)
    login_req_signal = pyqtSignal(str, str, socket)  # 로그인 요청 시그널
    duplicate_check_signal = pyqtSignal(str, socket)  # 이메일 중복 확인 시그널
    signup_req_signal = pyqtSignal(str, str, str, str, str, socket)  # 회원가입 요청 시그널 --> 이메일, 비밀번호
    post_upload_req_signal = pyqtSignal(str, str, str, str) # 이름, 제목, 내용, 사진경로(이메일은 db에서 불러옴)


    def __init__(self, parent):
        super().__init__()  # 클라이언트 접속, 접속종료, 메세지 수신시 사용되는 사용자 정의 시그널에 부모 윈도으이 함수를 슬롯으로 등록해 클래스간 신호 전달받기 위함
        self.parent = parent  # 부모윈도우 저장
        self.bListen = False  # 서버소켓이 리슨(접속 대기)상태인지 아닌지 저장
        self.clients = []  # 접속한 클라이언트들을 저장할 리스트 변수
        self.ip = []  # 접속한 클라이언트들의 ip 주소를 저장할 변수
        self.threads = []  # 클라이언트 접속, 데이터 수신시 보내는 시그널

        # db 클래스 연결
        self.data = DataClass()

        # 시그널 정리
        self.update_signal.connect(self.parent.updateClient)
        self.recv_signal.connect(self.parent.updateMsg)  # 메세지 수신 시그널
        self.login_req_signal.connect(self.handle_login_request)  # 로그인 요청
        self.duplicate_check_signal.connect(self.handle_duplicate_check)  # 이메일 중복 확인 요청
        # self.duplicate_check_signal.connect(self.handle_duplicate_check)
        self.signup_req_signal.connect(self.hanle_signup_request)
        self.post_upload_req_signal.connect(self.post_upload_request)

    def __del__(self):  # 서버소켓 클래스 객체가 파괴될 때 호출되는 소멸자. stop() 함수 사용해 대기중인 서버 소켓 종료
        self.stop()

    def start(self, ip, port):  # 부모 윈도우의 서버 실행 버튼을 누르면 호출되는 함수.
        self.server = socket(AF_INET, SOCK_STREAM)  # 전달 인자로 ip 주소와 port 번호를 전달 받는다. (ipv4, 연결지향형 소켓으로 만든다)
        '''ip는 네트워크에서 해당 기기의 인터넷 주소를 의미, port는 해당 기기 내의 연결 번호를 의미. '''

        try:
            self.server.bind((ip, port))
        except Exception as e:  # bind()에서 오류가 발생하면 exept 구문으로 들어와 오류 메세지를 출력
            print('Bind Error : ', e)
            return False
        else:  # 오류가 없다면 서버소켓을 리슨상태로 대기하기 위한 쓰레드를 생성하고 실행함
            self.bListen = True
            self.t = Thread(target=self.listen, args=(self.server,))
            self.t.start()
            print('[서버 응답 대기중...]')

        return True

    def stop(self):  # 서버 소켓을 닫는 함수
        self.bListen = False
        if hasattr(self, 'server'):
            self.server.close()
            print('Server Stop')

    def listen(self, server):  # 쓰레드에서 호출되는 함수
        while self.bListen:
            server.listen(5)  # 생성된 소켓을 리슨 상태(접속대기)로 만든 후
            try:
                client, addr = server.accept()  # accept()함수를 호출해 블럭(정지)상태로 만듬. accept는 클라이언트가 접속할 때까지 무한 대기하게 만듬
            except Exception as e:
                print('Accept() Error : ', e)
                break
            else:  # 만약 클라이언트가 접속한 경우 accept() 함수 탈출
                self.clients.append(client)  # 클라이언트 리스트에 저장
                self.ip.append(addr)  # 소켓, ip 주소 객체 변수에 저장
                self.update_signal.emit(addr, True)  # 부모윈도우에 클라이언트 접속을 알린 후
                t = Thread(target=self.receive, args=(addr, client))  # 접속한 클라이언트와 데이터 수신을 위한 쓰레드 생성
                self.threads.append(t)  # 쓰레드들 리스트에 저장. listen() 함수는 위 행동 무한 반복 수행해 클라이언트들이 접속할 때마다 새로운 연결을 반복적으로 수행함.
                t.start()  # 쓰레드 시작
                '''이렇게 쓰레드를 접속 할 때마다 생성하는 행위는 좋은 방법은 아니다. 쓰레드의 갯수는 한계가 존재하기 때문이다. thread Pool 을 이용해 쓰레드의 갯수를 제한해 처리하는 방식이 있다.'''

        self.removeAllClients()
        self.server.close()

    # Add other message type handlers as needed...
    def receive(self, addr, client):  # 클라이언트드가 접속할 때마다 생성되는 쓰레드에 의해 실행되는 함수
        while True:
            try:
                message_length = int.from_bytes(client.recv(4), byteorder='big')  # 메시지 길이를 수신하고 정수로 변환
                recv = client.recv(message_length)  # 그 다음에 메시지 본문을 수신
                # recv = client.recv(1024)  # 서버와 클라이언트가 1:1 연결이 이루어진 상태므로, recv()함수를 호출해 블럭 상태로 진입, 클라이언트가 보내는 메세지 대기
                print(recv)
            except Exception as e:
                print('Recv() Error :', e)
                break
            else:  # 만약 메세지를 수신했다면
                msg = str(recv, encoding='utf-8')  # 수신 메세지를 utf-8 문자열로 만들고 - 부모 윈도우에 전달
                if msg:
                    if msg.startswith('LOGIN_REQ'):  # 로그인 확인
                        msg_ = self.replace_msg(msg, 'LOGIN_REQ', ":")
                        email = msg_[0]
                        pw = msg_[1]
                        self.login_req_signal.emit(email, pw, client)

                    elif msg.startswith('CHECK_EMAIL'):  # 이메일 중복 확인
                        msg_ = msg.replace('CHECK_EMAIL', '')
                        email = msg_
                        self.duplicate_check_signal.emit(email, client)

                    elif msg.startswith("SIGNUP_REQ"):  # 회원가입 확인
                        msg_ = msg.replace('SIGNUP_REQ', '').split(':')
                        user_nm, user_pw, user_num, user_email, user_r_date = msg_[0], msg_[1], msg_[2], msg_[3], msg_[
                            4]
                        self.signup_req_signal.emit(user_nm, user_pw, user_num, user_email,
                                                    user_r_date, client)

                    elif msg.startswith('POST_REQ'):  # 게시글 업로드
                        msg_ = self.replace_msg(msg, 'POST_REQ', chr(0))
                        if len(msg_) == 4: # 제목, 글만 작성할 때
                            name, title, contents = msg_[1], msg_[2], msg_[3]
                            print(name, title, contents)

                        else: #제목, 글, 사진 모두 작성할 때
                            name, title, contents, img_base64 = msg_[1], msg_[2], msg_[3], msg_[4] # 제목, 내용, 사진 경로
                            while len(img_base64) % 4 != 0:  # 필요한 패딩을 추가
                                img_base64 += '='
                            img_data = base64.b64decode(img_base64)

                            # TODO 1. 사진 경로 지정해서 저장
                            # directory = "./Data/Board_img/" # 경로 지정하여 사진 저장 - 상대경로
                            directory = "C:\\Users\\KDT103\\Desktop\\coding\\0. 프로젝트\\개인프로젝트\\class_album\\Data\\receive_img\\" # 경로 지정하여 사진 저장 - 절대경로
                            if not os.path.exists(directory):
                                os.makedirs(directory)
                            img_path = directory + f'{title}.jpg' # 사진 이름 지정  TODO 3. 사진이름 추후 수정
                            with open(img_path, 'wb') as f:
                                f.write(img_data)

                            # TODO 2. DB 저장
                            self.post_upload_request(name=name, title=title, contents=contents, img_path=img_path)
                            print('[server.py] 클라이언트에서 받은 글쓰기 요청', msg_)
                            print('!! 서버 확인용', title, contents, img_path)

                    else:
                        # 채팅 부분
                        msg_ = msg.split(chr(0))  # 메세지 구분자로 나눔

                        # DB에 저장
                        name_, chat_ = msg_[0], msg_[1]
                        self.data.insert_chat_log(name_, msg_)  # DB에 이름과 로그, 시간 삽입

                        # 서버에 전달
                        self.send(name_, chat_)
                        self.recv_signal.emit(name_, chat_)  # 부모 윈도우에 전달하는 부분
                        print('[server.py]받은 메세지: ', addr, name_, chat_)

        # 이후 다시 무한 반복하며 recv() 함수를 호출해 다음 메세지 수신을 대기한다.
        self.removeClient(addr, client)

    def replace_msg(self, msg, header, split):
        """헤더 없애고 리턴"""
        msg = msg.replace(header, "").split(split)
        return msg

    def post_upload_request(self, name, title, contents, img_path=None):
        """게시글 제목과 내용을 db에 저장합니다."""
        email = self.data.return_user_email(name)
        time = self.data.return_datetime('date')
        self.data.insert_post_log(name=name, email=email, b_title=title,
                                  b_contents=contents, img_path=img_path, time=time)
        print('[server.py] 게시글 업로드 내용을 저장합니다.')
        pass

    def handle_login_request(self, email, password, client):
        # 로그인 요청 처리 구현
        print("[server.py]", email, password)
        vaild_id = self.data.check_login(id=email, pw=password)
        if vaild_id:
            print(f'[server.py] {vaild_id}님 로그인 완료!')
            self.data.insert_user_log(email=email)
            msg_ = f'vaild_id{vaild_id}'
        else:
            print('[server.py] 유효한 아이디가 아닙니다.')
            # msg_ = '[server.py] 유효한 아이디가 아닙니다.'
            msg_ = 'rejcet_login'
        self.send_spc_client(client, msg_)

    def handle_duplicate_check(self, email, client):
        """이메일 중복 확인 요청 처리 구현"""
        if not self.data.check_user_email(email):  # db class에 연결해 이메일이 존재하는지 확인
            self.send_spc_client(client, 'avlbl_email')  # 유효한 이메일
        else:
            self.send_spc_client(client, 'n_avlbl_email')  # 유효하지 않은 이메일

    def hanle_signup_request(self, user_nm, pw, user_num, email, r_date, c_socket):
        """회원정보 저장"""
        self.data.insert_user_info(user_nm=user_nm, email=email, pw=pw, rdate=r_date,
                                   user_num=user_num)  # 회원정보 TB_USER에 저장
        print('[server.py] 회원정보가 저장되었습니다.')

    def send(self, name, msg):  # 클라이언트가 보낸 데이터 수신 시, 연결된 모든 클라이언트들에게 해당 메세지를 보내는 역할(broadcast)을 담당.
        try:
            for c in self.clients:
                print('[서버] 보내는 클라이언트 소켓', c)
                s_ = chr(0)
                name_chat = f"{name}{s_}{msg}"
                c.send(name_chat.encode())
        except Exception as e:
            print('Send() Error : ', e)

    def send_spc_client(self, client, msg):
        """특정 클라이언트들에게만 신호를 보낸다."""
        try:
            client.send(msg.encode())
        except Exception as e:
            print('[server.py] 특정 클라이언트 정보 전달 오류: ', e)

    def removeClient(self, addr, client):  # 클라이언트의 연결이 끊어진 경우, 부모 윈도우로 이를 알림
        # find closed client index
        idx = -1
        for k, v in enumerate(self.clients):
            if v == client:
                idx = k
                break

        client.close()
        self.ip.remove(addr)
        self.clients.remove(client)

        del (self.threads[idx])
        self.update_signal.emit(addr, False)  # 부모 윈도우로 이를 알리는 부분
        self.resourceInfo()

    def removeAllClients(self):  # 모든 클라이언트의 접속을 끊는 역할. 주로 서버를 종료
        for c in self.clients:
            c.close()

        for addr in self.ip:
            self.update_signal.emit(addr, False)

        self.ip.clear()
        self.clients.clear()
        self.threads.clear()

        self.resourceInfo()

    def resourceInfo(self):  # 몇 개의 서버-클라이언트간 연결이 생성되었는지 콘솔창에 정보 출력
        print('Number of Client ip\t: ', len(self.ip))
        print('Number of Client socket\t: ', len(self.clients))
        print('Number of Client thread\t: ', len(self.threads))
