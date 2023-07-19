from UI.UI_mainwidget import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFrame, QLayout
from category_widget import Category
from list_widget import ListItem
from Page import PageBtn
from datetime import datetime


class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.init_UI() # 카테고리 버튼 추가
        self.add_post()



    def init_UI(self):
        """기본으로 들어갈 ui를 설정합니다."""
        # 카테고리 버튼 왼쪽에 추가
        for category in ['home', 'login', 'register', 'messenger']:  # 홈버튼, 로그인버튼, 회원가입 버튼
            image_path = f'./img/ui_img/{category}.png'
            new_category = Category(image_path, category, self)
            self.main_category.addWidget(new_category)
            if category == 'home':
                new_category.change_backgrond_color()

        # btn = PageBtn(lay=self.main_paging, txt=f'{i}')
        # self.main_paging.addWidget(btn.btn_return())
        arrow_list = ['<<', '<', '>', '>>']

        # 버튼 생성
        for i in arrow_list[:2]:
            btn = PageBtn(lay=self.main_paging, txt=f'{i}')
            self.main_paging.addWidget(btn.btn_return())
        for i in range(1, 5):
            btn = PageBtn(lay=self.main_paging, txt=f'{i}')
            self.main_paging.addWidget(btn.btn_return())
        for i in arrow_list[2:]:
            btn = PageBtn(lay=self.main_paging, txt=f'{i}')
            self.main_paging.addWidget(btn.btn_return())


    def move_page(self, c_name):
        """스택위젯 페이지 이동"""
        pages_dict = {
            'home': self.content_page,
            'login': self.login_page,
            'register': self.register_page,
            'messenger': self.chat_page
        }
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

        cnt = 1
        for i in range(10):
            sample_list = ListItem(str(cnt), '테스트 제목 제목이 아아주 길 수 있습니다. 테스트 제목', '이름', f'{date_format}', self)
            sample_list.set_contents_bar()
            cnt += 1
            print('1. 메인페이지 타입', type(self.main_page_contents))
            self.main_page_contents.addWidget(sample_list)

        # if click_event is not None:
        #     print(click_event)
        #     self.move_to_contents(list_title.title)

    def move_to_contents(self, title):
        """클릭한 페이지로 이동합니다."""
        # 내용들 숨기기
        self.search_btn.setVisible(False)
        self.search_lineedit.setVisible(False)
        self.clear_layout(self.main_page_contents)  # 레이아웃 지우기
        self.contents_title.setText(title)
        pass

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
