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


class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.data = DataClass()

        self.setupUi(self)
        self.add_post()  # 글 내용 리스트 추가
        self.event_connect()  # 클릭 시그널 연결
        self.init_UI()  # 카테고리 버튼 추가

        # self.var_init()

    # def var_init(self):
    #     self.data = DataClass()

    # == 글 작성 부분
    def write_contents(self):
        """글 쓰기 눌렀을 때 발생하는 이벤트 모음"""
        self.clear_layout(self.main_page_contents)  # 레이아웃 지워주고
        write_mode = BoardWrite()
        # img_btn, img_lab = write_mode.r_img_upload_btn()
        # img_btn.clicked.connect(self.upload_image(img_lab))
        self.main_page_contents.addWidget(write_mode)

    def upload_image(self, img_lab):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setNameFilter("Images (*.png *.jpg)")

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            pixmap = QPixmap(file_path)
            img_lab.setPixmap(pixmap.scaled(img_lab.size(), aspectRatioMode=Qt.KeepAspectRatio))

    # == ui 기본값 넣기
    # 카테고리 버튼
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

    def move_paging(self, btn_txt):
        """선택한 버튼에 따라 페이지를 이동시킨다."""
        # btn_move_dict = {
        #     '<'
        #
        # }
        print(btn_txt)

    # -- 클릭 이벤트 발생 모음

    def event_connect(self):
        """버튼 시그널 연결"""
        self.write_contents_btn.clicked.connect(self.write_contents)
        self.reply_btn.clicked.connect(self.write_reply)

    def write_reply(self):
        """댓글 작성하는 부분"""
        pass

    def move_to_contents(self, number, title, writer, write_date):
        """클릭한 페이지로 이동합니다."""

        # 내용들 숨기기
        self.search_btn.hide()
        self.search_lineedit.hide()
        self.write_contents_btn.hide()

        # 레이아웃 비우기
        self.clear_layout(self.main_page_contents)
        self.clear_layout(self.main_paging)

        # 라벨에 타이틀 넣기
        self.contents_title.setText(title)

        # 내용 채우기
        read_mode = BoardRead(title=title, writer=writer, img_path=None, contents='어쩌구 저쩌구', write_time='7월 19일')
        self.main_page_contents.addWidget(read_mode)

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
