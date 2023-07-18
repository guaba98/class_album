from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from UI.UI_category import Ui_Form

class Category(QWidget, Ui_Form):
    def __init__(self, img_path, c_name, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.category_name = c_name

        self.img_lab.setPixmap(QPixmap(f'{img_path}'))
        self.name_lab.setText(c_name)

        self.frame.mousePressEvent = self.move_page

    def move_page(self, event):
        """스택위젯 페이지 이동"""
        pages_dict = {
            'home': self.parent.main_page,
            'login': self.parent.login_page,
            'register': self.parent.register_page,
        }

        self.parent.stackedWidget.setCurrentWidget(pages_dict[self.category_name])


