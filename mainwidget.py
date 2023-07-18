from UI.UI_mainwidget import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from category_widget import Category

class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.init_UI()



    def init_UI(self):
        # 홈 버튼 추가

        for category in ['home', 'login', 'register']:
            image_path = f'./img/ui_img/{category}.png'
            new_category = Category(image_path, category, self)
            self.main_category.addWidget(new_category)






