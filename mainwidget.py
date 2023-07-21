# 모듈
from PyQt5.QtWidgets import QMainWindow, QLayout, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import Qt
from datetime import datetime

# 클래스
from UI.UI_mainwidget import Ui_MainWindow
from Source.category_widget import Category
from Source.list_widget import ListItem
from Source.Page import PageBtn
from Source.Board import BoardRead, BoardWrite
from Source.DataClass import DataClass
from Source.dig_warning import DialogWarning
from Source.msgbox import MsgBox
import client


class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # 객체 생성
        self.data = DataClass()
        self.dig_warning = DialogWarning()
        self.c = client.ClientSocket(self)  # 클라이언트 소켓 생성

        '''
        컴퓨터 ip : 192.168.56.1
        컴퓨터 자리 고정 ip : 10.10.20.103
        노트북 ip: 172.16.2.73
        '''

        # ip, port 지정
        self.ip = '192.168.56.1'  # 임시지정
        self.port = 1121
        self.login_state = None
        self.user_name = None

        # 함수 연결
        self.connectClicked()
        self.add_post()  # 글 내용 리스트 추가
        self.event_connect()  # 클릭 시그널 연결
        self.init_UI()  # 초기설정(카테고리 버튼 추가 등)
        # self.var_init() # 변수

    # -- 변수
    # def var_init(self):
    #     """변수 들어가는 함수"""
    #     self.login_state = False
    #     self.user_name = None

    # -- 버튼 시그널 발생 모음
    def event_connect(self):
        """버튼 시그널 연결"""

        # 페이지 이동
        self.register_login_lab.mousePressEvent = lambda event: self.stackedWidget.setCurrentWidget(
            self.login_page)  # 로그인 페이지로 이동
        self.register_btn.mousePressEvent = lambda event: self.stackedWidget.setCurrentWidget(
            self.register_page)  # 회원가입 페이지로 이동

        # 이벤트 연결
        self.write_contents_btn.clicked.connect(self.write_contents)  # 글 작성하기
        self.reply_btn.clicked.connect(self.write_reply)  # 댓글 작성

        # 시그널 연결
        self.chat_send_btn.clicked.connect(self.sendMsg)  # 메세지 보내기
        self.chat_lineedit.returnPressed.connect(self.sendMsg)  # 메세지 보내기(엔터)
        self.login_start_btn.clicked.connect(self.sendLogin)  # 로그인 확인
        self.register_admit_btn.clicked.connect(self.sendRegister)  # 회원가입 유효성 확인 -> 회원가입

    ## 네트워크 #################################################################
    # -- 네트워크 관련
    def connectClicked(self):
        """연결 상태 확인하는 함수"""
        if not self.c.bConnect:
            ip = self.ip
            port = self.port
            if self.c.connectServer(ip, int(port)):
                print('[메인] 접속 종료')
            else:
                self.c.stop()
                self.chat_lineedit.clear()
                print('[메인] 접속')
        else:
            self.c.stop()
            self.chat_lineedit.clear()
            print('[메인] 접속')

    def __del__(self):
        """연결 끊겼을 때 클라이언트 소켓을 멈춘다."""
        self.c.stop()

    def updateMsg(self, name, msg):
        """메세지 박스로 메세지 내용을 추가한다. """

        self.data.insert_chat_log(name, msg)
        log = f'{name}: {msg}'
        self.chat_main_contents.addWidget(MsgBox(log, send_time=None, parent=None))
        print('[mainwidget.py] 업데이트된 메세지: ', log)

    def updateDisconnect(self):
        print('[mainwidget.py] 접속')

        # -- 서버에 요청

    def sendMsg(self):
        if self.login_state:
            sendmsg = self.chat_lineedit.text()
            # TODO 사용자의 이름을 넣는 부분 체크
            # name =
            self.c.send(msg=sendmsg, name=self.user_name)
            print('[mainwidget.py] 내가 보낸 메세지: ', self.user_name, sendmsg)
        else:
            self.dig_warning.set_dialog_type(1, t_type='unable_chat')  # 회원만 채팅이 가능함
            self.dig_warning.exec_()
        self.chat_lineedit.clear()

    def sendLogin(self):
        email = self.email_lineedit.text()
        password = self.password_lineedit.text()
        self.c.login_request(email, password)

    def sendDbEmail(self, email):
        """이메일 전송(클라이언트 소켓으로)"""
        self.c.check_vaild_email(email)

    def sendRegister(self):
        """회원가입 요청 하는 부분"""

        # 이름, 이메일, 핸드폰 번호, 비밀번호
        name, email, cell_num, password = \
            self.register_name_lineedit.text(), self.register_email_lineedit.text(), self.register_cellphone_num_lineedit.text(), self.register_password_lineedit.text()

        # 유효성 체크
        if not self.validate_register_form(name, email, cell_num, password):
            return

        # 이메일 중복 확인
        self.sendDbEmail(email)

    def show_dialog_window(self, num, type, txt=None):
        """경고 팝업창 단순화 시키기"""
        self.dig_warning.set_dialog_type(num, t_type=type, text=txt)
        self.dig_warning.exec_()

    # -- 서버에서 정보 받는 부분
    def receive_login(self, msg):
        """여기에 팝업화면을 보여줍니다."""
        print('[mainwidget.py] 로그인 리턴값: ', msg)

        if msg != 'rejcet_login':
            user_nm = msg.replace('vaild_id', "")
            self.user_name = user_nm  # 유저 이름
            self.dig_warning.set_dialog_type(bt_cnt=1, text=f'{user_nm}님 로그인 완료!')
            self.dig_warning.exec_()
            self.login_state = True  # 로그인 여부
            self.stackedWidget.setCurrentWidget(self.main_page)  # 로그인 시 메인 페이지로 이동
            #  로그인 되면 로그인 회원가입 창이 안 뜨고 로그아웃 할 수 있는 부분 추가
        else:
            self.dig_warning.set_dialog_type(bt_cnt=1, t_type='reject_login')
            self.dig_warning.exec_()

    def receive_email(self, email):
        """이메일이 존재하는지 리턴값을 받습니다."""
        print('[mainwidget.py] receive_email 함수 ', email)
        if email != 'avlbl_email':
            self.show_dialog_window(1, 'used_email')
        else:
            # 회원가입 가능할 때 다이얼로그 띄우기 및 DB 저장
            self.show_dialog_window(1, 'register_cmplt')
            date_ = self.data.return_datetime('date')

            # 이름, 이메일, 핸드폰 번호, 비밀번호
            name, email_, cell_num, password = \
                self.register_name_lineedit.text(), self.register_email_lineedit.text(), self.register_cellphone_num_lineedit.text(), self.register_password_lineedit.text()

            # 회원가입 연결
            self.c.register_request(username=name, password=password,
                                    user_num=cell_num, email=email_, r_date=date_)

            # 회원가입 연결 후 로그인 창으로 이동
            self.stackedWidget.setCurrentWidget(self.login_page)

    # 회원가입 유효성 체크 ###################################################

    # -- 회원가입 유효성 체크 부분(메인에서 할 수 있는 부분)
    def validate_register_form(self, name, email, cell_num, password):
        """회원가입 유효성 여부를 체크"""
        print(f'이름:{name}, 이메일:{email}, 핸드폰:{cell_num}, 비번:{password}')  # 확인용
        if not name:
            self.show_dialog_window(1, 'name_input')
            return False
        elif not email:
            self.show_dialog_window(1, 'email_input')
            return False
        elif cell_num == '--':
            self.show_dialog_window(1, 'cell_num_input')
            return False
        elif not password:
            self.show_dialog_window(1, 'pw_input')
            return False
        elif not self.check_valid_email(email):
            self.show_dialog_window(1, 'not_valid_email')
            return False
        elif not self.check_password_recheck():
            self.show_dialog_window(1, 'pw_recheck')
            return False
        return True

    def check_valid_email(self, email):
        """이메일 특수문자 확인"""
        list_ = ['@', '.']
        for i in list_:
            if i not in email:
                return False
        return True

    def check_password_recheck(self):
        """비밀번호 동일한지 체크"""
        if self.register_password_lineedit.text() == \
                self.register_password_recheck_lineedit.text():
            return True
        else:
            return False

    def clearMsg(self):
        self.chat_lineedit.clear()

    # 글 작성 및 읽기 부분 ###########################################################

    # -- 글 작성 부분
    def write_contents(self):
        """글 쓰기 눌렀을 때 발생하는 이벤트 모음"""
        self.clear_layout(self.main_page_contents)  # 레이아웃 지워주고
        write_mode = BoardWrite()
        # img_btn, img_lab = write_mode.r_img_upload_btn()
        # img_btn.clicked.connect(self.upload_image(img_lab))
        self.main_page_contents.addWidget(write_mode)

    def upload_image(self, img_lab):
        """이미지 업로드하기"""
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setNameFilter("Images (*.png *.jpg)")

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            pixmap = QPixmap(file_path)
            img_lab.setPixmap(pixmap.scaled(img_lab.size(), aspectRatioMode=Qt.KeepAspectRatio))

    # -- 글 읽기 부분
    def move_to_contents(self, number, title, writer, write_date):
        """클릭한 페이지로 이동합니다."""

        # 초기설정
        self.active_btn(False)  # 다른 버튼들 내용들 숨기기
        self.clear_layout(self.main_page_contents)  # 레이아웃 비우기
        self.contents_title.setText(title)  # 라벨에 타이틀 넣기

        # 조건
        c_ = f"BOARD_TITLE = '{title}'"
        contents = self.data.return_specific_data(table_name='TB_NOTICE_BOARD', column='BOARD_CONTENTS', conditon=c_)
        img_ = self.data.return_specific_data(table_name='TB_NOTICE_BOARD', column='BOARD_IMG', conditon=c_)

        # 내용 채우기
        read_mode = BoardRead(title=title, writer=writer, img_path=img_, contents=contents, write_time=write_date)
        self.main_page_contents.addWidget(read_mode)

    def add_post(self):
        # 카테고리에 리스트위젯 추가
        date_format = datetime.now().strftime("%Y-%m-%d")
        list_title = ListItem('No', '테스트 제목', '이름', '날짜', self)
        list_title.set_title_bar()
        self.main_page_contents.addWidget(list_title)

        c_df = self.data.return_df('TB_NOTICE_BOARD')
        self.c_df_cnt = len(c_df.index)  # 글 갯수

        for i in range(self.c_df_cnt):
            index = c_df.iloc[i]['BOARD_ID']
            title = c_df.iloc[i]['BOARD_TITLE']
            name = c_df.iloc[i]['USER_NAME']
            write_date = c_df.iloc[i]['UPDATE_TIME']

            print(index, title, name, write_date)
            sample_list = ListItem(number=str(index), title=title, writer=name,
                                   write_date=write_date, parent=self)
            sample_list.set_contents_bar()
            self.main_page_contents.addWidget(sample_list)

    def move_page(self, c_name):
        """스택위젯 페이지 이동"""
        pages_dict = {
            'home': self.content_page,
            'login': self.login_page,
            'register': self.register_page,
            'messenger': self.chat_page
        }
        if c_name == 'home':
            self.clear_layout(self.main_page_contents)
            self.clear_layout(self.main_paging)
            self.active_btn(True)
            self.add_post()

        # 여기에 리스트위젯 추가하는 부분
        if c_name in ['register', 'login']:
            self.stackedWidget.setCurrentWidget(pages_dict[c_name])
        else:
            self.sub_stackedwidget.setCurrentWidget(pages_dict[c_name])

    # -- 댓글 작성
    def write_reply(self):
        """댓글 작성하는 부분"""
        pass

    # -- ui 관련 부분 #################################################
    def move_paging(self, btn_txt):
        """선택한 버튼에 따라 페이지를 이동시킨다."""
        # btn_move_dict = {
        #     '<'
        #
        # }
        print(btn_txt)

    def init_UI(self):
        """기본으로 들어갈 ui를 설정합니다."""
        # 카테고리 버튼 왼쪽에 추가
        for category in ['home', 'login', 'register', 'messenger']:  # 홈버튼, 로그인버튼, 회원가입 버튼
            image_path = f'./img/ui_img/{category}.png'
            new_category = Category(image_path, category, self)
            self.main_category.addWidget(new_category)
            if category == 'home':
                new_category.change_backgrond_color()

        self.make_arrow_button(self.c_df_cnt)  # 화살표 번호 생성
        self.reply_lineedit.hide()
        self.reply_btn.hide()
        self.register_cellphone_num_lineedit.setInputMask('000-0000-0000;_')

    # 화살표 버튼
    def make_arrow_button(self, cnt):
        # 화살표 버튼 생성하기
        arrow_list = ['<<', '<', '>', '>>']

        # 버튼 생성
        for i in arrow_list[:2]:
            btn = PageBtn(txt=f'{i}', parent=self)
            self.main_paging.addWidget(btn.btn_return)
        for i in range(1, cnt):
            btn = PageBtn(txt=f'{i}', parent=self)
            self.main_paging.addWidget(btn.btn_return)
        for i in arrow_list[2:]:
            btn = PageBtn(txt=f'{i}', parent=self)
            self.main_paging.addWidget(btn.btn_return)

    def active_btn(self, type):
        if type:
            self.search_btn.show()
            self.search_lineedit.show()
            self.write_contents_btn.show()
            self.reply_lineedit.hide()
            self.reply_btn.hide()
            self.make_arrow_button(self.c_df_cnt)
            self.contents_title.setText('게시판 제목')
        else:
            self.search_btn.hide()
            self.search_lineedit.hide()
            self.write_contents_btn.hide()
            self.reply_lineedit.show()
            self.reply_btn.show()
            self.clear_layout(self.main_paging)

    def clear_layout(self, layout: QLayout):
        """레이아웃 안의 모든 객체를 지웁니다."""
        if layout is None or not layout.count():
            return
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()

            if widget is not None:
                widget.setParent(None)
            # 아이템이 레이아웃일 경우 재귀 호출로 레이아웃 내의 위젯 삭제
            else:
                self.clear_layout(item.layout())
