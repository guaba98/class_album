from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from UI.UI_category import Ui_Form
from list_widget import ListItem
from datetime import datetime

class Category(QWidget, Ui_Form):
    def __init__(self, img_path, c_name, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.category_name = c_name

        self.img_lab.setPixmap(QPixmap(f'{img_path}'))
        self.name_lab.setText(c_name)
        self.frame.setObjectName(f'{c_name}_frame')

        # 버튼 이벤트
        self.frame.mousePressEvent = self.move_page

    def c_frame(self):
        return self.frame


    def move_page(self, event):
        """스택위젯 페이지 이동"""
        pages_dict = {
            'home': self.parent.content_page,
            'login': self.parent.login_page,
            'register': self.parent.register_page,
            'messenger': self.parent.chat_page
        }
        if self.category_name in ['register', 'login']:
            self.parent.stackedWidget.setCurrentWidget(pages_dict[self.category_name])
        else:
            self.parent.sub_stackedwidget.setCurrentWidget(pages_dict[self.category_name])

        # return self.category_name

        # # 버튼 표시 및 레이아웃 지우기
        # self.parent.search_btn.setVisible(True)
        # self.parent.search_lineedit.setVisible(True)
        # self.clear_layout(self.parent.main_page_contents)
        # cnt = 1
        # for i in range(10):
        #     sample_list = ListItem(str(cnt), '테스트 제목 제목이 아아주 길 수 있습니다. 테스트 제목', '이름', f'날짜', self)
        #     sample_list.set_contents_bar()
        #     cnt += 1
        #     self.parent.main_page_contents.addWidget(sample_list)


    def change_backgrond_color(self):
        self.frame.setStyleSheet('background-color: #82B3F4')

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



