from UI.UI_mainwidget import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFrame
from category_widget import Category
from list_widget import ListItem

from datetime import datetime



class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.init_UI()

        # 테스트 부분

        self.category_frames = self.main_category.findChildren(QFrame)
        for frame in self.category_frames:
            print(frame.objectName())

    def init_UI(self):

        # 카테고리 버튼 왼쪽에 추가
        for category in ['home', 'login', 'register']:  # 홈버튼, 로그인버튼, 회원가입 버튼
            image_path = f'./img/ui_img/{category}.png'
            new_category = Category(image_path, category, self)
            self.main_category.addWidget(new_category)
            if category == 'home':
                new_category.change_backgrond_color()



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
            self.main_page_contents.addWidget(sample_list)

    # def clear_layout(self, layout: QLayout):
    #     if layout is None or not layout.count():
    #         return
    #     while layout.count():
    #         item = layout.takeAt(0)
    #         widget = item.widget()
    #
    #         if widget is not None:
    #             widget.setParent(None)
    #         # 아이템이 레이아웃일 경우 재귀 호출로 레이아웃 내의 위젯 삭제
    #         else:
    #             self.clear_layout(item.layout())
